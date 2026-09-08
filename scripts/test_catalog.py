"""Regression checks for untrusted stream URLs and endpoint fallbacks (no network)."""
import io
import contextlib
import json
import tempfile
from pathlib import Path
import unittest
from unittest.mock import patch
import build_catalog as catalog
import finalize_catalog as finalizer


def dns(host, *_args, **_kwargs):
    ip = {'localhost':'127.0.0.1','internal.example':'10.0.0.1'}.get(host,'93.184.216.34')
    return [(2,1,6,'',(ip,443))]

class Process:
    def __init__(self, body): self.stdout=io.BytesIO(body)
    def terminate(self): pass
    def wait(self, **kwargs): pass

AUDIO=b'HTTP/1.1 200 OK\r\nContent-Type: audio/mpeg\r\n\r\n'+b'\xff\xfb'+b'x'*4094

class StreamSafety(unittest.TestCase):
    @patch.object(catalog.socket,'getaddrinfo',side_effect=dns)
    def test_rejects_private_credentials_and_insecure_urls(self,_dns):
        for url in ('http://radio.example/live','https://localhost/live','https://internal.example/live',
                    'https://user:pass@radio.example/live','https://radio.example/\nheader','https://radio.example:bad/live'):
            with self.subTest(url=url), patch.object(catalog.subprocess,'Popen') as request:
                self.assertFalse(catalog.probe_endpoint(url)['ok']);request.assert_not_called()

    def test_mixed_public_private_dns_rejected(self):
        with patch.object(catalog.socket,'getaddrinfo',return_value=[(2,1,6,'',('93.184.216.34',443)),(2,1,6,'',('192.168.1.1',443))]):
            self.assertFalse(catalog.safe_url('https://radio.example/live'))

    def test_multicast_is_not_a_public_stream_endpoint(self):
        with patch.object(catalog.socket,'getaddrinfo',return_value=[(2,1,6,'',('224.0.0.1',443))]):
            self.assertFalse(catalog.safe_url('https://radio.example/live'))

    @patch.object(catalog.socket,'getaddrinfo',side_effect=dns)
    def test_audio_sample_pins_dns_and_keeps_tls_verification(self,_dns):
        with patch.object(catalog.subprocess,'Popen',return_value=Process(AUDIO)) as request:
            result=catalog.probe_endpoint('https://radio.example/live')
            self.assertTrue(result['ok']);self.assertEqual(result['verification']['sampleBytes'],4096)
            args=request.call_args.args[0]
            self.assertIn('radio.example:443:93.184.216.34',args)
            self.assertIn('--noproxy',args)
            self.assertNotIn('-k',args);self.assertNotIn('-L',args)

    @patch.object(catalog.socket,'getaddrinfo',side_effect=dns)
    def test_redirect_cannot_downgrade_or_reach_private_network(self,_dns):
        for destination in ('http://radio.example/audio','https://internal.example/audio'):
            with patch.object(catalog.subprocess,'Popen',return_value=Process(f'HTTP/1.1 302 Found\r\nLocation: {destination}\r\n\r\n'.encode())) as request:
                self.assertFalse(catalog.probe_endpoint('https://radio.example/live')['ok'])
                self.assertEqual(request.call_count,1)

    @patch.object(catalog.socket,'getaddrinfo',side_effect=dns)
    def test_relative_redirect_is_verified(self,_dns):
        with patch.object(catalog.subprocess,'Popen',side_effect=[Process(b'HTTP/1.1 302 Found\r\nLocation: /audio\r\n\r\n'),Process(AUDIO)]):
            result=catalog.probe_endpoint('https://radio.example/live')
            self.assertTrue(result['ok']);self.assertEqual(result['finalUrl'],'https://radio.example/audio')

    @patch.object(catalog.socket,'getaddrinfo',side_effect=dns)
    def test_pages_manifests_and_short_samples_fail(self,_dns):
        for body in (AUDIO.replace(b'audio/mpeg',b'text/html'), AUDIO[:100],
                     b'HTTP/1.1 200 OK\r\nContent-Type: audio/mpeg\r\n\r\n<html>'+b'x'*4096,
                     AUDIO.replace(b'audio/mpeg',b'application/vnd.apple.mpegurl')):
            with patch.object(catalog.subprocess,'Popen',return_value=Process(body)):
                self.assertFalse(catalog.probe_endpoint('https://radio.example/live')['ok'])

    def test_fallback_resolved_endpoint_after_original_failure(self):
        with patch.object(catalog,'probe_endpoint',side_effect=[{'ok':False},{'ok':True,'verification':{},'finalUrl':'https://other.example/live'}]):
            result=catalog.probe({'url':'https://radio.example/player','url_resolved':'https://other.example/live'})
            self.assertEqual(result['_url'],'https://other.example/live')

    def test_http_endpoints_are_only_tested_over_https(self):
        self.assertEqual(catalog.endpoint_urls({'url':'http://radio.example:8000/live#fragment'}),['https://radio.example:8000/live'])
        self.assertEqual(catalog.endpoint_urls({'url':'https://radio.example/live','url_resolved':'https://radio.example/live'}),['https://radio.example/live'])

class UncappedRefresh(unittest.TestCase):
    def test_full_country_survives_refresh_and_cached_resume(self):
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp);out=root/'data';doc=root/'documents';doc.mkdir()
            records=[{'stationuuid':str(i),'countrycode':'US','name':'Same name',
                      'url':f'https://radio.example/{i}','tags':'jazz','language':'english'} for i in range(130)]
            records.append({**records[0],'stationuuid':'duplicate'})
            (doc/'source-snapshot.json').write_text(json.dumps(records))
            (doc/'supplemental-stations.json').write_text('[]')
            iso=[{'cca2':'US','latlng':[40,-100],'name':{'common':'United States'},'region':'Americas'}]
            def result(url):
                return {'ok':True,'finalUrl':url,'verification':{'checkedAt':catalog.NOW.isoformat(),
                        'contentType':'audio/mpeg','sampleBytes':4096,'publicAddressPinned':True}}
            with patch.object(catalog,'OUT',out),patch.object(catalog,'DOC',doc), \
                 patch.object(catalog.sys,'argv',['build_catalog.py','--cached-source']), \
                 patch.object(catalog,'fetch',side_effect=[{'features':[]},iso,{'features':[]},iso]), \
                 patch.object(catalog,'probe_endpoint',side_effect=result) as probe,contextlib.redirect_stdout(io.StringIO()):
                catalog.main()
                data=json.loads((out/'catalog.json').read_text())
                self.assertEqual(len(data['stations']),130)
                self.assertEqual(data['countries'][0]['stationCount'],130)
                self.assertEqual(probe.call_count,130)
                catalog.main()
                self.assertEqual(probe.call_count,130,'Resume should reuse fresh evidence')
                report=json.loads((doc/'discovery-report.json').read_text())
                self.assertEqual(report['recordExclusions']['duplicate_stream'],1)
                self.assertEqual(report['metadata']['checkedEndpoints'],130)

class LocationAudit(unittest.TestCase):
    def test_old_coordinates_stay_retired_and_current_audit_is_repeatable(self):
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp);out=root/'data';doc=root/'documents';out.mkdir();doc.mkdir()
            base={'country':'US','name':'Station','locationSource':'directory'}
            stations=[{**base,'id':'unlocated','lat':None,'lon':None},
                      {**base,'id':'near','lat':0,'lon':3}, {**base,'id':'conflict','lat':0,'lon':10}]
            data={'metadata':{'generatedAt':'current','stationCount':3,'verification':'sample','ranking':'clicks'},
                  'countries':[{'code':'US','name':'United States','stationCount':3}], 'stations':stations}
            (out/'catalog.json').write_text(json.dumps(data))
            (doc/'location-audit.json').write_text(json.dumps({'catalogGeneratedAt':'old',
                'movedToCountryLocation':[{'id':'unlocated','sourceLat':70,'sourceLon':100}],
                'excludedForConflictingCountry':[{'id':'historic'}]}))
            geo={'features':[{'properties':{'ISO_A2_EH':'US'},'geometry':{'type':'Polygon',
                  'coordinates':[[[-1,-1],[1,-1],[1,1],[-1,1],[-1,-1]]]}}]}
            iso=[{'cca2':'US','name':{'common':'United States'}}]
            with patch.object(finalizer,'OUT',out),patch.object(finalizer,'DOC',doc), \
                 patch.object(finalizer,'fetch',side_effect=[geo,iso,geo,iso]),contextlib.redirect_stdout(io.StringIO()):
                finalizer.main();first=json.loads((out/'catalog.json').read_text())
                finalizer.main();second=json.loads((out/'catalog.json').read_text())
            self.assertEqual(first,second)
            self.assertEqual({s['id'] for s in second['stations']},{'near','unlocated'})
            audit=json.loads((doc/'location-audit.json').read_text())
            self.assertEqual([s['id'] for s in audit['excludedForConflictingCountry']],['conflict'])
            self.assertEqual([s['id'] for s in audit['movedToCountryLocation']],['near'])

if __name__=='__main__':unittest.main()
