#!/usr/bin/env python3
"""Package only the verified static build; never include source snapshots or dependencies."""
import pathlib, shutil, zipfile, hashlib
root=pathlib.Path(__file__).resolve().parents[1]
source=root/'website/dist'
assert (source/'index.html').is_file() and (source/'data/catalog.json').is_file()
upload=root/'upload'
upload.mkdir(exist_ok=True)
shutil.copytree(source,upload,dirs_exist_ok=True)
# Remove stale generated assets so the folder and ZIP represent the same build.
for f in upload.rglob('*'):
    if f.is_file() and not (source/f.relative_to(upload)).is_file():f.unlink()
with zipfile.ZipFile(root/'radio-atlas-upload.zip','w',zipfile.ZIP_DEFLATED) as z:
    for f in sorted(source.rglob('*')):
        if f.is_file():z.write(f,f.relative_to(source))
with zipfile.ZipFile(root/'radio-atlas-upload.zip') as z:
    expected={str(f.relative_to(source)) for f in source.rglob('*') if f.is_file()}
    assert set(z.namelist())==expected
    assert {str(f.relative_to(upload)) for f in upload.rglob('*') if f.is_file()}==expected
    for name in expected:
        assert z.read(name)==(source/name).read_bytes()==(upload/name).read_bytes()
digest=hashlib.sha256((root/'radio-atlas-upload.zip').read_bytes()).hexdigest()
(root/'documents/RELEASE-SHA256.txt').write_text(f'{digest}  radio-atlas-upload.zip\n')
print(f'Ready: {upload} and radio-atlas-upload.zip')
for relative in ('public/data','public','src'):
    p=root/relative
    if p.is_dir() and not any(p.iterdir()):p.rmdir()
