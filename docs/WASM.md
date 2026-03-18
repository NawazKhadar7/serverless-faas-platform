# Optional Wasmtime backend

Install wasmtime separately. wasm_runtime.add loads an import-free module, enables fuel, limits memory and avoids WASI. This helper has not been executed here. It demonstrates runtime configuration; production requires module-size limits, compile-time budgets and careful export validation.
