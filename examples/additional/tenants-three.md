# tenants-three

Alternate three invocations between two tenants.

Each tenant owns a worker and one is reused once.

Family: tenants. Size: 3. Deterministic seed: 910910.

Run from the project directory:

~~~powershell
python -B examples/additional/run_cases.py --case tenants-three
~~~

Add --json to inspect returned metrics and output.

The adjacent expected file specifies the following metric conditions:

| Metric | Condition |
| --- | --- |
| requests | equals 3 |
| ok | equals 3 |
| limited | equals 0 |
| timeouts | equals 0 |
| failed | equals 0 |
| accounted | equals true |
| results_correct | equals true |
| worker_starts | equals 2 |
| warm_reuses | equals 1 |
| untrusted_code_enabled | equals false |

Scope: Trusted predefined handlers in local worker processes.

These inputs are synthetic. See [project limitations](../../docs/LIMITATIONS.md).
