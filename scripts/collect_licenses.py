#!/usr/bin/env python3
import json, pathlib, subprocess
root=pathlib.Path(__file__).resolve().parents[1]
modules=root/'website/node_modules'
out=root/'website/public/THIRD-PARTY-NOTICES.txt'
names=['react','react-dom','scheduler','leaflet','lucide-react','@base-ui/react','@base-ui/utils','@floating-ui/core','@floating-ui/dom','@floating-ui/react-dom','@floating-ui/utils','tabbable','use-sync-external-store','clsx','tailwind-merge','class-variance-authority']
sections=['RADIO ATLAS — THIRD-PARTY NOTICES\n\nMap boundaries: Natural Earth (public domain). https://www.naturalearthdata.com/\nCountry/territory metadata: mledoze/countries (ODbL 1.0). https://github.com/mledoze/countries\nStation metadata: Radio Browser public directory. https://www.radio-browser.info/\nAudio remains the property of its respective broadcasters and rights holders.']
for name in names:
    p=modules/name
    if not p.exists(): continue
    meta=json.loads((p/'package.json').read_text())
    licenses=[f for f in p.iterdir() if f.is_file() and f.name.lower().startswith(('license','licence','copying'))]
    sections.append(f'\n{name} {meta["version"]}\n'+('\n'.join(f.read_text(errors='replace') for f in licenses) or f'License: {meta.get("license","see package source")}'))
country_license=subprocess.run(['curl','-fLsS','--max-time','30','https://raw.githubusercontent.com/mledoze/countries/master/LICENSE'],capture_output=True,check=True).stdout.decode()
sections.append('\nCountry data: ODbL 1.0\n'+country_license)
out.write_text('\n\n'.join(sections)+'\n')
print(f'Wrote {out.name}: {out.stat().st_size} bytes')
