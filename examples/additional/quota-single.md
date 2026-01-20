# quota-single

Exercise the minimum invocation quota.

The single invocation succeeds.

Family: quota. Size: 1. Deterministic seed: 910905.

Run from the project directory:

~~~powershell
python -B examples/additional/run_cases.py --case quota-single
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
