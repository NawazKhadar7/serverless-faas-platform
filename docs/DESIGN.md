# Design

Separate user identity, quotas and worker state. Never eval user strings. An untrusted platform needs an audited runtime with OS resource limits and syscall isolation; that boundary is not represented by Python processes.
