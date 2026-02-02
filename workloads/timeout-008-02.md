# timeout-008-02

Terminate a worker whose sleep handler exceeds its deadline.

Input scale: 8; deterministic random seed: 195.
Run `python scripts/demo.py --case workloads/timeout-008-02.case.json`.
The adjacent expected file specifies acceptance conditions independently from the implementation.
A successful run validates these conditions, not a production latency or capacity guarantee.

Inspect `metrics` and `output` in the returned JSON. Increase the input scale only after reading
`docs/LIMITATIONS.md`; do not extrapolate synthetic timing to hardware or external services.
