#!/usr/bin/env python3
from pathlib import Path
import json

old = 'https://russelldudek.github.io/AIAction/'
new = 'https://russelldudek.github.io/'

for name in [
    '120-day-plan.html',
    'cover-letter.html',
    'index.html',
    'interview-brief.html',
    'resume.html',
    'workflow-precedent-review.html',
    '.github/workflows/publish.yml',
]:
    path = Path(name)
    text = path.read_text(encoding='utf-8').replace(old, new)
    if name == 'index.html':
        text = text.replace('Candidate vision: https://russelldudek.github.io/', 'Portfolio: https://russelldudek.github.io/')
    if name == 'cover-letter.html':
        old_paragraph = 'I created a role-specific candidate vision at <a href="https://russelldudek.github.io/"><strong>https://russelldudek.github.io/</strong></a>. It includes an interactive Applied AI Reporter, a 120-day entry plan, an interview thesis, and a Workflow Precedent Review canvas so you can inspect how I would approach the work rather than rely on claims alone.'
        new_paragraph = 'I prepared a role-specific candidate vision package with this application. It includes an interactive Applied AI Reporter, a 120-day entry plan, an interview thesis, and a Workflow Precedent Review canvas so you can inspect how I would approach the work rather than rely on claims alone.'
        text = text.replace(old_paragraph, new_paragraph)
    path.write_text(text, encoding='utf-8')

manifest = Path('artifact-manifest.json')
data = json.loads(manifest.read_text(encoding='utf-8'))
data['state'] = 'blocked'
data['candidate_vision'] = None
data['portfolio_url'] = new
data['publication'] = {
    'branch': 'main',
    'candidate_vision': None,
    'portfolio_url': new,
    'repository_status': 'published',
    'live_status': 'blocked - GitHub Pages not enabled'
}
manifest.write_text(json.dumps(data, indent=2) + '\n', encoding='utf-8')

audit = Path('campaign-audit.md')
text = audit.read_text(encoding='utf-8')
text = text.replace(
    'State: published. Live verification remains a separate gate until GitHub Pages reports a successful deployment.',
    'State: blocked. Readable source and validated PDFs are published; live verification is blocked because GitHub Pages is not enabled.'
)
section = '''
## Verified URL Correction
- The unverified role-specific Pages URL was removed from candidate-facing documents because Pages is not enabled.
- Resume, cover letter, briefs, plans, and the site footer now use Russell's verified public portfolio URL: https://russelldudek.github.io/
- The cover letter describes the role-specific candidate package without claiming that it is live.
- PDFs were regenerated and exact page contracts revalidated after the correction.
'''
if '## Verified URL Correction' not in text:
    text = text.rstrip() + '\n' + section
else:
    text = text.split('## Verified URL Correction')[0].rstrip() + '\n' + section
audit.write_text(text.rstrip() + '\n', encoding='utf-8')

print('Verified portfolio URL correction applied.')
