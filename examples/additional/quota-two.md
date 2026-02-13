# quota-two

Send two invocations through a one-request quota.

The second is limited before worker execution.

Family: quota. Size: 2. Deterministic seed: 910906.

Run from the project directory:

~~~powershell
python -B examples/additional/run_cases.py --case quota-two
~~~

Add --json to inspect returned metrics and output.

The adjacent expected file specifies the following metric conditions:

| Metric | Condition |
| --- | --- |
| requests | equals 2 |
| ok | equals 1 |
| limited | equals 1 |
| timeouts | equals 0 |
| failed | equals 0 |
| accounted | equals true |
| results_correct | equals true |
| worker_starts | equals 1 |
| warm_reuses | equals 0 |
| untrusted_code_enabled | equals false |

Scope: Trusted predefined handlers in local worker processes.

These inputs are synthetic. See [project limitations](../../docs/LIMITATIONS.md).
