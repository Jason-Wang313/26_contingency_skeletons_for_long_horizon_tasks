$ErrorActionPreference = "Continue"

$Root = Split-Path -Parent $PSScriptRoot
$Paper = Join-Path $Root "paper"
$DownloadsPdf = "C:/Users/wangz/Downloads/26.pdf"
$Status = Join-Path $Paper "build_status.md"

Set-Content -Path $Status -Value "# Build Status`n`n- Starting pdflatex/bibtex build." -Encoding UTF8

Push-Location $Paper

pdflatex -interaction=nonstopmode -halt-on-error main.tex
if ($LASTEXITCODE -ne 0) {
  Add-Content -Path $Status -Value "`n- First pdflatex failed with exit code $LASTEXITCODE. See paper/main.log."
  Pop-Location
  exit 0
}

bibtex main
if ($LASTEXITCODE -ne 0) {
  Add-Content -Path $Status -Value "`n- BibTeX failed with exit code $LASTEXITCODE. See paper/main.blg."
  Pop-Location
  exit 0
}

pdflatex -interaction=nonstopmode -halt-on-error main.tex
if ($LASTEXITCODE -ne 0) {
  Add-Content -Path $Status -Value "`n- Second pdflatex failed with exit code $LASTEXITCODE. See paper/main.log."
  Pop-Location
  exit 0
}

pdflatex -interaction=nonstopmode -halt-on-error main.tex
if ($LASTEXITCODE -ne 0) {
  Add-Content -Path $Status -Value "`n- Third pdflatex failed with exit code $LASTEXITCODE. See paper/main.log."
  Pop-Location
  exit 0
}

Pop-Location

if (Test-Path (Join-Path $Paper "main.pdf")) {
  New-Item -ItemType Directory -Force -Path (Split-Path -Parent $DownloadsPdf) | Out-Null
  Copy-Item -LiteralPath (Join-Path $Paper "main.pdf") -Destination $DownloadsPdf -Force
  Add-Content -Path $Status -Value "`n- Build succeeded."
  Add-Content -Path $Status -Value "`n- Copied final PDF to $DownloadsPdf."
} else {
  Add-Content -Path $Status -Value "`n- Build ended without paper/main.pdf."
}

exit 0
