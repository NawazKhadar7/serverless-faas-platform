# cold-single

Invoke one handler with cold execution.

The worker is retired after the invocation.

Family: cold. Size: 1. Deterministic seed: 910903.

Run from the project directory:

~~~powershell
python -B examples/additional/run_cases.py --case cold-single
~~~

Add --json to inspect returned metrics and output.

The adjacent expected file specifies the following metric conditions:

| Metric | Condition |
| --- | --- |
| requests | equals 1 |
| ok | equals 1 |
| limited | equals 0 |
| timeouts | equals 0 |
| failed | equals 0 |
| accounted | equals true |
| results_correct | equals true |
| worker_starts | equals 1 |
| warm_reuses | equals 0 |
| untrusted_code_enabled | equals false |

Scope: Trusted predefined handlers in local worker processes.

These inputs are synthetic. See [project limitations](../../docs/LIMITATIONS.md).
