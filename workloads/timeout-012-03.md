# timeout-012-03

Terminate a worker whose sleep handler exceeds its deadline.

Input scale: 12; deterministic random seed: 196.
Run `python scripts/demo.py --case workloads/timeout-012-03.case.json`.
The adjacent expected file specifies acceptance conditions independently from the implementation.
A successful run validates these conditions, not a production latency or capacity guarantee.

Inspect `metrics` and `output` in the returned JSON. Increase the input scale only after reading
`docs/LIMITATIONS.md`; do not extrapolate synthetic timing to hardware or external services.
