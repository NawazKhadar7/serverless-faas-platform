# Algorithms

Map tenants to reusable child processes. Admission happens before startup. Parent uses a pipe with a deadline; timeout retires and kills the worker. Warm requests reuse a process, while cold mode retires after each request. Wasmtime uses fuel with no WASI/host imports. Reference: https://bytecodealliance.github.io/wasmtime-py/ .
