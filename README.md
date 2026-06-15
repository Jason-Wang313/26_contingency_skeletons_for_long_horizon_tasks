# Guarded Contingency Skeletons for Long-Horizon Robot Tasks

Anonymous research artifact for paper 26 in the robotics/embodied-intelligence batch.

## Final V3 State

- Canonical PDF: `C:/Users/wangz/Downloads/26.pdf`.
- Page count: 25.
- PDF bytes: 371778.
- PDF SHA256: `A36A75140750716A0D4E61DD4D59A7251AF27F6780FC0DDC5FA522AF61D8AAB9`.
- Local `paper/main.pdf`: intentionally absent after export.
- Full-scale suite: 79,305 method-condition rows over 10,135 deterministic cases, seed 26026, zero plot failures.

## Contents

- `docs/full_scale_execution_plan.md`: detailed v3 execution plan written before the full-scale pass.
- `experiments/full_scale_gcs.py`: RAM-light full-scale v3 experiment runner.
- `results/full_scale/`: streamed rows, summaries, generated TeX tables, metadata, and counterexamples.
- `figures/full_scale/`: generated PDF/PNG figures used by the final manuscript.
- `paper/main.tex`: final 25-page ICLR-style manuscript source.
- `docs/validation_report.json`: final export and verification record.

Legacy v1/v2 artifacts remain in `results/`, `paper/figures/`, and `experiments/run_guarded_skeletons.py` for history, but the final submission evidence is the v3 full-scale suite.

## Reproduce

Regenerate the full-scale evidence:

```powershell
python experiments/full_scale_gcs.py
```

Build the paper and copy the final PDF to `C:/Users/wangz/Downloads/26.pdf`:

```powershell
powershell -ExecutionPolicy Bypass -File scripts/build_paper.ps1
```

The final build command sequence used for verification was:

```powershell
cd paper
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

## Headline V3 Findings

- Family A: eager GCS cost 58.45 versus replan-on-failure 92.51 and linear default 312.54.
- Family A: eager GCS uses 293,649 nodes on average versus 79.10 billion for no-sharing GCS.
- Probe-cost boundary: at probe cost 6.0, eager GCS costs 157.60 and loses to replan by 48.53.
- Guard-error boundary: at 100% guard error, eager GCS costs 149.26 and loses to replan by 35.34.
- Coverage boundary: missing relevant guards produce many failures, so the formal coverage claim is inactive even when synthetic cost stays below replan.

The final claim is a synthetic representation mechanism for known, cheap, safe, calibrated, locally sparse guards. It does not claim real-robot deployment, learned guard discovery, production TAMP superiority, POMDP optimality, or safety certification.
