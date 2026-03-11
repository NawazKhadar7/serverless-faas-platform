# Isolation

Only fixed trusted handlers run in Python workers. Deadlines terminate child processes, but they do not limit memory or syscalls. The included Dockerfile runs unprivileged but is not a per-function security sandbox. Use an audited WebAssembly/container/microVM design before enabling submitted code.
