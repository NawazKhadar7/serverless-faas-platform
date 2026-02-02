# failure-three

Invoke the predefined failing handler three times.

Failures are accounted for and the worker is reused.

Family: failure. Size: 3. Deterministic seed: 910909.

Run from the project directory:

~~~powershell
python -B examples/additional/run_cases.py --case failure-three
~~~

Add --json to inspect returned metrics and output.

The adjacent expected file specifies the following metric conditions:

| Metric | Condition |
| --- | --- |
| requests | equals 3 |
| ok | equals 0 |
| limited | equals 0 |
| timeouts | equals 0 |
| failed | equals 3 |
| accounted | equals true |
| results_correct | equals true |
| worker_starts | equals 1 |
| warm_reuses | equals 2 |
| untrusted_code_enabled | equals false |

Scope: Trusted predefined handlers in local worker processes.

These inputs are synthetic. See [project limitations](../../docs/LIMITATIONS.md).
