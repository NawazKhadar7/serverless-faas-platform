# Additional scenarios for serverless-faas-platform

Ten runnable scenarios cover small inputs, odd sizes, and behavior boundaries in the existing reference implementation.

This directory contains 10 input JSON files, 10 metric-oracle JSON files, 10 scenario notes, this guide, and the runner (32 files).

Run from the project directory with Python 3.10 or later and the dependencies already listed in requirements.txt.

~~~powershell
python -B examples/additional/run_cases.py --list
python -B examples/additional/run_cases.py
python -B examples/additional/run_cases.py --case warm-single --json
~~~

The runner exits with zero only when all selected scenarios pass. --json includes metrics and output or a failure reason for each scenario.

Each .case.json is paired with a .expected.json containing equality checks or numeric bounds for the existing syslab.common.check helper.
Scenario notes explain the selected boundaries. Fixed seeds make inputs repeatable; expected files contain assertions rather than recorded timings.

| Scenario | Family | Size | Purpose |
| --- | --- | --- | --- |
| warm-single | warm | 1 | Invoke one trusted sum handler. |
| warm-three | warm | 3 | Invoke three sums for the same tenant. |
| cold-single | cold | 1 | Invoke one handler with cold execution. |
| cold-three | cold | 3 | Invoke three handlers with cold execution. |
| quota-single | quota | 1 | Exercise the minimum invocation quota. |
| quota-two | quota | 2 | Send two invocations through a one-request quota. |
| quota-three | quota | 3 | Exercise quota rounding with three invocations. |
| timeout-single | timeout | 1 | Invoke the predefined sleep handler with a short deadline. |
| failure-three | failure | 3 | Invoke the predefined failing handler three times. |
| tenants-three | tenants | 3 | Alternate three invocations between two tenants. |

Scope: Trusted predefined handlers in local worker processes.

Supplemental inputs have their own runner, so the existing workload discovery and its 36-case suite retain their current behavior.
Bytecode generation is disabled. Reports go to standard output; storage and model artifacts use the reference code's temporary directories.

See [limitations](../../docs/LIMITATIONS.md) and [running instructions](../../docs/RUNNING.md).
