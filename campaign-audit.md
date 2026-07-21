# Candidate Campaign Audit

State: published. Live verification remains a separate gate until GitHub Pages reports a successful deployment.

## Intended gates
- Factual integrity: verified candidate evidence only
- Narrative continuity: one thesis across site and documents
- Brand fidelity: plain-text identity with documented logo exception
- Candidate-facing confidentiality: no private orchestration names or source repository references
- Accessibility: semantic controls, keyboard-native buttons, focusable links, reduced motion
- Responsive behavior: desktop, laptop, tablet, mobile
- Print: exact 2 / 1 / 4 / 3 / 2 page contracts
- Downloads: same-origin PDF download links with explicit filenames
- Publication: public main branch and live route/PDF verification

## Automated publication verification
- Exact PDF page counts validated in GitHub Actions
- Candidate files committed to main
- Pages deployment attempted from the validated workspace
