# timeout-single

Invoke the predefined sleep handler with a short deadline.

The worker is retired after the request times out.

Family: timeout. Size: 1. Deterministic seed: 910908.

Run from the project directory:

~~~powershell
python -B examples/additional/run_cases.py --case timeout-single
~~~

Add --json to inspect returned metrics and output.

The adjacent expected file specifies the following metric conditions:

| Metric | Condition |
| --- | --- |
| requests | equals 1 |
| ok | equals 0 |
| limited | equals 0 |
| timeouts | equals 1 |
| failed | equals 0 |
| accounted | equals true |
| results_correct | equals true |
| worker_starts | equals 1 |
| warm_reuses | equals 0 |
| untrusted_code_enabled | equals false |

Scope: Trusted predefined handlers in local worker processes.

These inputs are synthetic. See [project limitations](../../docs/LIMITATIONS.md).
