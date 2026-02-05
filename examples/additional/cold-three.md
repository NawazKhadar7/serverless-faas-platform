# cold-three

Invoke three handlers with cold execution.

Each invocation starts its own worker without reuse.

Family: cold. Size: 3. Deterministic seed: 910904.

Run from the project directory:

~~~powershell
python -B examples/additional/run_cases.py --case cold-three
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
| worker_starts | equals 3 |
| warm_reuses | equals 0 |
| untrusted_code_enabled | equals false |

Scope: Trusted predefined handlers in local worker processes.

These inputs are synthetic. See [project limitations](../../docs/LIMITATIONS.md).
