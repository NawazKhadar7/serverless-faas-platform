# tenants-024-06

Keep reusable workers separate for two tenants.

Input scale: 24; deterministic random seed: 261.
Run `python scripts/demo.py --case workloads/tenants-024-06.case.json`.
The adjacent expected file specifies acceptance conditions independently from the implementation.
A successful run validates these conditions, not a production latency or capacity guarantee.

Inspect `metrics` and `output` in the returned JSON. Increase the input scale only after reading
`docs/LIMITATIONS.md`; do not extrapolate synthetic timing to hardware or external services.
