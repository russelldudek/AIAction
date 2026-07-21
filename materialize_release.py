#!/usr/bin/env python3
from __future__ import annotations

import base64
import io
import shutil
import zipfile
from pathlib import Path

root = Path(__file__).resolve().parent
bundle = root / '.release-bundle'
parts = sorted(bundle.glob('part-*.txt'))
if not parts:
    raise SystemExit('No release bundle parts found')
encoded = ''.join(part.read_text(encoding='ascii').strip() for part in parts)
payload = base64.b64decode(encoded)
with zipfile.ZipFile(io.BytesIO(payload)) as archive:
    for member in archive.infolist():
        target = (root / member.filename).resolve()
        if root not in target.parents and target != root:
            raise SystemExit(f'Unsafe release path: {member.filename}')
    archive.extractall(root)
shutil.rmtree(bundle)
Path(__file__).unlink()
print('Living Precedent Engine release materialized.')
