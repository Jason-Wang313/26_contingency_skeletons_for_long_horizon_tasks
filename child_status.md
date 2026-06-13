# Child Status

Stage: v2 hardening complete

Latest actions:
- Added v2 guard-assumption stress for expensive probes and noisy guards.
- Rebuilt the paper with a visible v2 hardening note and stress table.
- Copied the canonical PDF to `C:/Users/wangz/Downloads/26.pdf`.
- Removed local `paper/main.pdf` after canonical copy.

Commands run:
- `python experiments/run_guarded_skeletons.py`
- `powershell -ExecutionPolicy Bypass -File scripts/build_paper.ps1`

Findings:
- GitHub URL: `https://github.com/Jason-Wang313/26_contingency_skeletons_for_long_horizon_tasks`
- Downloads PDF exists at `C:/Users/wangz/Downloads/26.pdf`, size 200396 bytes.
- Desktop copies are absent.
- Local `paper/main.pdf` is absent.
- `docs/related_work_matrix.csv` has 5147 data rows plus header.
- V2 probe-cost stress: probe cost 6.00 makes GCS 14.79 worse than replan-on-failure.
- V2 guard-error stress: 100% flipped guards make noisy GCS 4.66 worse than replan-on-failure.

Failures:
- Initial v2 stress run timed out because it recomputed full baselines too often.
- Original v1 build script left local `paper/main.pdf`.

Recovery steps:
- Optimized the stress runner to reuse the per-seed replan baseline.
- Patched the build script to return nonzero on failures and remove local `paper/main.pdf` after copying.

Next:
- Commit and push v2 hardening, then update batch trackers.

End time: 2026-06-13 04:45:39 +01:00
PDF exists: True
