# Multi-Tenant Serverless FaaS Platform

A local trusted-handler execution platform with per-tenant process reuse, quotas, failure responses and enforced deadlines.

This is newly generated educational reference code based on a concept in the supplied PDF.
It has **165 non-empty source, test, configuration, workload and documentation files**.
It is a prototype for study and extension, not evidence of previous deployment or measured large-scale performance.

## Quick start

Requires Python 3.10+; the default path uses the standard library.

```sh
python scripts/demo.py
python scripts/run_tests.py
python scripts/benchmark.py
python scripts/serve.py --port 8080
```

Open http://127.0.0.1:8080 for the workload dashboard. `scripts/demo.py --case workloads/<id>.case.json`
executes one workload and checks its independent acceptance conditions. `benchmark.py` prints actual local timings.

## Implemented scope

Multiprocessing worker pool, predefined validated handlers, tenant-owned reuse, bounded process count, admission quotas, wall-clock deadlines with termination, and optional import-free Wasmtime add module with fuel and memory limits.

## Limits and optional runtimes

Default Python workers run trusted registered functions only; process separation is NOT an untrusted-code sandbox. No arbitrary snippets, Firecracker, containerd, cloud deployment or millisecond cold-start guarantee. Requests are sequential in workloads, and quotas are lifetime-per-experiment rather than rate windows. Wasmtime optional path is unexecuted because the dependency is unavailable.

All bundled data are synthetic. No credentials, pretrained model weights, historical commits, or fabricated benchmark results are included.
See `docs/PROVENANCE.md`, `docs/TESTING.md`, and the bundle's validation report for evidence and omissions.
