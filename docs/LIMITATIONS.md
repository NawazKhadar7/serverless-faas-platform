# Limitations

Default Python workers run trusted registered functions only; process separation is NOT an untrusted-code sandbox. No arbitrary snippets, Firecracker, containerd, cloud deployment or millisecond cold-start guarantee. Requests are sequential in workloads, and quotas are lifetime-per-experiment rather than rate windows. Wasmtime optional path is unexecuted because the dependency is unavailable.
