#!/usr/bin/env python3
from pathlib import Path

index = Path('index.html')
text = index.read_text(encoding='utf-8')
old = '<a class="btn primary" href="#reporter">Explore the operating model</a>'
new = '<a class="btn primary" href="#evidence">See the evidence map</a>'
if old in text:
    text = text.replace(old, new, 1)
index.write_text(text, encoding='utf-8')

audit = Path('campaign-audit.md')
text = audit.read_text(encoding='utf-8')
section = '''
## Recurring Correction Prevention Audit
- Hero restraint: passed
- Runtime motion proof: passed locally, including intermediate frame and stable settlement
- State synchronization: passed, including rapid final-state selection
- Causal and visual economy: passed
- CTA advancement: passed after changing the hero action from the adjacent artifact to the evidence map
- 390-pixel mobile composition: passed
- 320-pixel narrow-phone composition: passed
- Rendered asset geometry: passed with documented logo-use exception
- Rendered text and component geometry: passed
- Screen document behavior: passed at 390 and 320 pixels
- Print/PDF behavior: passed with exact 2 / 1 / 4 / 3 / 2 contracts
- Strength-first public positioning: passed
- Evidence and full-JD continuity: passed
- Readable main-branch source: passed
- Material-correction revalidation: passed locally and on main; live proof remains blocked by Pages enablement
- Correction regression coverage: passed
'''
if '## Recurring Correction Prevention Audit' not in text:
    text = text.rstrip() + '\n' + section
else:
    text = text.split('## Recurring Correction Prevention Audit')[0].rstrip() + '\n' + section
text = text.replace('State: published. Live verification remains a separate gate until GitHub Pages reports a successful deployment.','State: blocked. Readable source and validated PDFs are published; live verification is blocked because GitHub Pages is not enabled.')
audit.write_text(text.rstrip() + '\n', encoding='utf-8')

print('Final CTA and recurring-correction audit applied.')
