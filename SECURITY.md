# Security scope

The dashboard binds to loopback and accepts bundled workload IDs only. Do not expose it publicly without authentication, request limits and TLS.
Do not submit or execute untrusted Python code. The registered handlers are fixed and validated. Process separation is operational isolation only; a hosted untrusted service requires an audited sandbox and OS limits.
No real identities, payments, patient records or secrets belong in bundled workloads.
Report bugs privately to the repository owner; no contact address is assumed.
