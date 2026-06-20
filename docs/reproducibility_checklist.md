# Reproducibility Checklist

- [x] Main simulator is `src/guarded_skeletons.py`.
- [x] Full-scale v3 experiment script is `experiments/full_scale_gcs.py`.
- [x] Full-scale outputs are under `results/full_scale/`.
- [x] Generated final figures are under `figures/full_scale/`.
- [x] Generated final TeX tables are under `results/full_scale/tex/`.
- [x] Final paper source is `paper/main.tex`.
- [x] Build script is `scripts/build_paper.ps1`.
- [x] Canonical PDF path is `C:/Users/wangz/Downloads/26.pdf`.
- [x] Canonical PDF pages: 25.
- [x] Canonical PDF bytes: 371778.
- [x] Canonical PDF SHA256: `7D31075ED0F6CC9DF9AFFE14C3D7D9621EF43285D64E20E281B7E3C02E582BC9`.
- [x] Local `paper/main.pdf` removed after canonical copy.
- [x] Visible Desktop PDF copies are absent.
- [x] VLA-style link boxes verified with pypdf inventory and rendered-page
  visual inspection.

Recommended verification commands:

```powershell
python -m py_compile .\experiments\full_scale_gcs.py
python experiments\full_scale_gcs.py
cd paper
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdfinfo C:\Users\wangz\Downloads\26.pdf
Get-FileHash C:\Users\wangz\Downloads\26.pdf -Algorithm SHA256
```

Legacy v1/v2 outputs remain for audit history, but the final paper uses the v3 full-scale evidence.
