#!/usr/bin/env python3
from pathlib import Path
import base64
import json
import zlib

parts = sorted(Path('.campaign-bundle').glob('bundle.*'))
if not parts:
    raise SystemExit('Campaign bundle chunks were not found.')

encoded = ''.join(path.read_text(encoding='utf-8').strip() for path in parts)
files = json.loads(zlib.decompress(base64.b64decode(encoded)))

for name, content in files.items():
    path = Path(name)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding='utf-8')

print(f'Materialized {len(files)} campaign files.')
