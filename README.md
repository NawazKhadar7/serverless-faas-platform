# Multi-Tenant Serverless FaaS Platform

A local trusted-handler execution platform with per-tenant process reuse, quotas, failure responses and enforced deadlines.

## 1. Overview

Function execution must balance reuse, tenant admission and bounded execution time. This local platform makes those controls visible through predefined trusted handlers and worker processes, without treating process separation as an untrusted-code sandbox.

**Project type:** educational reference implementation. **Repository contents:** 165 non-empty source, test, configuration, workload and documentation files, including 36 synthetic workload scenarios.

## 2. Core Features — Why They Matter

- **Tenant-owned reuse:** Reuses a worker for the same tenant to distinguish cold starts from warm execution.
- **Bounded scheduling:** Limits process count and applies tenant admission quotas.
- **Deadline enforcement:** Terminates workers that exceed wall-clock deadlines and returns explicit failure responses.
- **Optional WebAssembly helper:** Includes an import-free Wasmtime add module with fuel and memory limits.

## 3. Tech Stack & Architecture

| Layer | Technology | Implementation status |
| --- | --- | --- |
| Default execution | Python 3.10+, multiprocessing and pipes | Runnable trusted-handler path |
| Admission | Local tenant quotas and bounded scheduler | Reference policy; sequential bundled request workloads |
| Optional backend | Wasmtime and WebAssembly text module | Optional dependency; skipped in bundle validation |

### How the components fit together

Tenant admission passes eligible requests to a bounded scheduler. A tenant-owned worker receives a predefined handler request through a process pipe and returns a result. Deadline enforcement retires timed-out workers; the optional WebAssembly helper is a separate backend.

| Component | Responsibility |
| --- | --- |
| [src/syslab/tenant.py](src/syslab/tenant.py) | Tenant admission and quota state. |
| [src/syslab/scheduler.py](src/syslab/scheduler.py) | Bounded scheduling and worker reuse. |
| [src/syslab/worker.py](src/syslab/worker.py) | Predefined trusted handlers and process communication. |
| [src/syslab/wasm_runtime.py](src/syslab/wasm_runtime.py) | Optional Wasmtime execution helper. |

See [Architecture](docs/ARCHITECTURE.md) and [Algorithms](docs/ALGORITHMS.md) for implementation notes.

### Scope and limitations

Default Python workers run trusted registered functions only; process separation is NOT an untrusted-code sandbox. No arbitrary snippets, Firecracker, containerd, cloud deployment or millisecond cold-start guarantee. Requests are sequential in workloads, and quotas are lifetime-per-experiment rather than rate windows. Wasmtime optional path is unexecuted because the dependency is unavailable.

## 4. Getting Started / Installation

**Prerequisites:** Python 3.10+. The default reference uses Python's standard library. No API keys or external services are needed for the default sample.

Download/extract this project or clone its repository, then open a terminal in the `serverless-faas-platform` folder. Create an isolated environment:

```sh
python -m venv .venv
```

Activate it on Linux/macOS:

```sh
source .venv/bin/activate
```

Or on Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Install the declared Python dependencies and run the demo:

```sh
python -m pip install -r requirements.txt
python scripts/demo.py
```

Check behavior and collect timings on your own machine:

```sh
python scripts/run_tests.py
python scripts/benchmark.py
```

The original bundle validation recorded **23 passing tests; 1 optional test skipped** for this project and **36 accepted workload scenarios**. These are local reference checks, not production or hardware benchmarks. See [Testing](docs/TESTING.md) and [Benchmark notes](docs/BENCHMARKS.md).

## 5. Usage Examples

### Run a reproducible workload

The bundled [sample request](examples/request.json) contains:

```json
{
  "family": "warm",
  "id": "warm-004-01",
  "seed": 101,
  "size": 4
}
```

Run the corresponding workload and check its independent acceptance conditions:

```sh
python scripts/demo.py --case workloads/warm-004-01.case.json
```

Expected `metrics` excerpt from the verified local run; the complete JSON also includes `output`:

```json
{
  "metrics": {
    "accounted": true,
    "failed": 0,
    "limited": 0,
    "ok": 4,
    "requests": 4,
    "results_correct": true,
    "timeouts": 0,
    "untrusted_code_enabled": false,
    "warm_reuses": 3,
    "worker_starts": 1
  }
}
```

Four successful requests use one worker start and three warm reuses. untrusted_code_enabled=false confirms this example runs predefined trusted functions; these counts do not establish production latency or sandbox security.

The complete example is in [examples/response.json](examples/response.json). Floating-point last digits can vary across numeric environments.

### Explore through the local dashboard

```sh
python scripts/serve.py --port 8080
```

Open [http://127.0.0.1:8080](http://127.0.0.1:8080), select a workload and choose **Run and check**. The server listens on loopback and is intended for local inspection.

With the server running, a second terminal can call its workload inspection API:

```sh
curl "http://127.0.0.1:8080/api/run?id=warm-004-01"
```

This endpoint executes the bundled workload; it is not a production domain API.

## 6. Your Contributions / Research Alignment

### Implementation evidence

The following work areas are present in this reference and can be reviewed directly:

| Work area in this reference | Repository evidence |
| --- | --- |
| Tenant-owned reuse | [src/syslab/tenant.py](src/syslab/tenant.py) |
| Correctness and edge cases | [tests/](tests/) and [acceptance workloads](workloads/) |
| Reproducible evaluation | [scripts/demo.py](scripts/demo.py), [scripts/benchmark.py](scripts/benchmark.py), [testing notes](docs/TESTING.md) |

### Research alignment

The project connects cloud execution models with scheduling, resource control and runtime boundaries. It supports a research discussion about cold-start behavior, tenant fairness and the guarantees required for safe function hosting.

**A question to investigate:** How do reuse and quota policies affect measured latency and fairness, and what additional isolation is required before accepting untrusted functions?

This question is a proposed extension, not a completed research result. Evaluate it with controlled inputs, independent correctness checks and measurements tied to a reproducible configuration.

### Personal contribution record

This reference was generated from the supplied project concept. Personal authorship or research contributions have not been verified. For an MS application, document only the modules you actually changed, the design choices you can explain, and experiments you ran; link those claims to commits or reproducible reports. See [Provenance](docs/PROVENANCE.md).

All bundled inputs are synthetic. The repository does not establish historical development dates, prior deployment or published research.
