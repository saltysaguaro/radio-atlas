#!/usr/bin/env python3
"""Small context and bounded stream checks for the hourly research task."""
import argparse
import concurrent.futures
import datetime
import html
import json
from pathlib import Path
import re

from build_catalog import probe_endpoint

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / 'documents/COUNTRY_RADIO_RESEARCH.md'


def rows():
    result = []
    for line in LEDGER.read_text().splitlines():
        if re.match(r'^\| \d+ \| [A-Z]{2} \|', line):
            parts = [p.strip() for p in line.strip('|').split('|')]
            result.append(parts)
    assert len(result) >= 250 and len({r[1] for r in result}) == len(result)
    assert {'PS', 'EH', 'XK'} <= {r[1] for r in result}
    return result


def stations():
    return (json.loads((ROOT / 'website/public/data/catalog.json').read_text())['stations']
            + json.loads((ROOT / 'documents/supplemental-stations.json').read_text()))


def catalog_index():
    result = {}
    for station in stations():
        for key in ('url', 'url_resolved', '_finalUrl'):
            if station.get(key):
                result.setdefault(station[key], []).append({
                    k: station[k] for k in ('id', 'name', 'country')})
    return result


def prior_mentions(urls):
    # Scan on disk, never send the archive to the model. A mention is not proof
    # of duplication: it may be a failed or unresolved endpoint.
    files = [LEDGER] + sorted((ROOT / 'documents/research').rglob('*.md'))
    result = {url: [] for url in urls if url}
    for path in files:
        body = html.unescape(path.read_text())
        found = set(re.findall(r'https?://[^\s<>"`]+', body))
        found |= {u.rstrip('),.;|') for u in found}
        for url in result:
            if html.unescape(url) in found:
                result[url].append(str(path.relative_to(ROOT)))
    return result


def context():
    all_rows = rows()
    active = [r for r in all_rows if r[5] == 'in-progress']
    if len(active) > 1:
        raise ValueError('Multiple interrupted runs; reconcile before researching.')
    selected = active[0] if active else min(all_rows, key=lambda r: (int(r[4]), int(r[0])))
    current = [s for s in stations() if s['country'] == selected[1]]
    print(json.dumps({
        'country': selected[2], 'code': selected[1], 'runs': int(selected[4]),
        'status': selected[5], 'latestLog': selected[9],
        'completedRuns': sum(int(r[4]) for r in all_rows),
        'existingFeedCount': len(current),
        'existingNamesSample': [s['name'] for s in current[:20]],
        'limits': {'searchQueries': 6, 'sourcePages': 8, 'streamChecks': 10,
                   'researchMinutes': 4},
    }, ensure_ascii=False, indent=2))


def check(input_path, output_path):
    inputs = json.loads(input_path.read_text())
    if not isinstance(inputs, list) or not all(isinstance(x, str) for x in inputs):
        raise ValueError('Input must be a JSON array of stream URL strings.')
    inputs = list(dict.fromkeys(inputs))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    previous = json.loads(output_path.read_text()) if output_path.exists() else []
    seen = {r['url'] for r in previous}
    pending = [url for url in inputs if url not in seen]
    if len(seen | set(inputs)) > 10:
        raise ValueError('Maximum 10 unique stream inputs per run; reuse the same output file.')
    index = catalog_index()

    def probe(url):
        record = {'url': url, 'checkedAt': datetime.datetime.now(datetime.timezone.utc).isoformat()}
        matches = index.get(url, [])
        if matches:
            return {**record, 'catalogMatches': matches, 'result': {'skipped': 'already_in_catalog'}}
        try:
            result = probe_endpoint(url)
        except Exception as error:
            result = {'ok': False, 'reason': type(error).__name__ + ': ' + str(error)[:160]}
        return {**record, 'result': result,
                'catalogMatches': index.get(result.get('finalUrl'), [])}

    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        for record in executor.map(probe, pending):
            previous.append(record)
            temporary = output_path.with_suffix(output_path.suffix + '.tmp')
            temporary.write_text(json.dumps(previous, ensure_ascii=False, indent=2) + '\n')
            temporary.replace(output_path)
    urls = {r['url'] for r in previous} | {r['result'].get('finalUrl') for r in previous}
    mentions = prior_mentions(urls)
    for record in previous:
        record['priorResearchFiles'] = sorted(set(
            mentions.get(record['url'], []) + mentions.get(record['result'].get('finalUrl'), [])))
    output_path.write_text(json.dumps(previous, ensure_ascii=False, indent=2) + '\n')
    # All raw verification metadata stays in the file; stdout is deliberately small.
    print(json.dumps([{
        'url': r['url'], 'ok': r['result'].get('ok'),
        'reason': r['result'].get('reason', r['result'].get('skipped')),
        'catalogMatches': r['catalogMatches'], 'priorResearchFiles': r['priorResearchFiles'],
    } for r in previous], ensure_ascii=False))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    sub.add_parser('context')
    probe = sub.add_parser('check')
    probe.add_argument('input', type=Path)
    probe.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    if args.command == 'context':
        context()
    else:
        check(args.input, args.output)


if __name__ == '__main__':
    main()
