---
title: "execute"
description: "Execute a shell command directly on the host system."
source: "https://reference.langchain.com/python/deepagents/backends/local_shell/LocalShellBackend/execute"
category: "reference"
tags: [reference, deepagents, backends, local_shell, localshellbackend, execute]
---

# execute

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/local_shell/LocalShellBackend/execute)

Execute a shell command directly on the host system.

!!! danger "Unrestricted Execution"

    Commands are executed directly on your host system
    using `subprocess.Popen()` with `shell=True`. There is **no sandboxing,
    isolation, or security restrictions**. The command runs with
    your user's full permissions and can:

    - Access any file on the filesystem (regardless of `virtual_mode`)
    - Execute any program or script
    - Make network connections
    - Modify system configuration
    - Spawn additional processes
    - Install packages or modify dependencies

    **Always use Human-in-the-Loop (HITL) middleware when using this method.**

The command is executed using the system shell (`/bin/sh` or equivalent)
with the working directory set to the backend's `root_dir`.
Stdout and stderr are combined into a single output stream.

On POSIX systems, each command starts in a new session without sharing
the parent's controlling terminal. A timeout, an interruption such as
`KeyboardInterrupt`, and async cancellation all terminate the command's
process group with `SIGKILL`, then wait briefly for the shell process to
exit. A descendant that makes its own session or process group, for
example with `setsid`, leaves that group and is not killed. `nohup` alone
does not change the process group or protect against `SIGKILL`.

Async cancellation cleanup applies only when `execute` is not overridden.

On Windows, commands do not start in a new process group. Cleanup
terminates only the direct shell process, so descendants may continue
running after a timeout, an interruption, or async cancellation. A
descendant that inherits the output handles also keeps the pipes open, so
the command waits for the full timeout even after the shell itself exits.

## Signature

```python
execute(
    self,
    command: str,
    *,
    timeout: int | None = None,
) -> ExecuteResponse
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `command` | `str` | Yes | Shell command string to execute.  Examples: `"python script.py"`, `"ls -la"`, `"grep pattern file.txt"`  **Security:** This string is passed directly to the shell. Agents can execute arbitrary commands including pipes, redirects, command substitution, etc. |
| `timeout` | `int \| None` | No | Maximum time in seconds to wait for this command.  Overrides the default timeout set at init.  If `None`, uses the default. (default: `None`) |

## Returns

`ExecuteResponse`

`ExecuteResponse` containing:
- `output`: Combined stdout and stderr (stderr lines prefixed with `[stderr]`)
- `exit_code`: Process exit code (0 for success, non-zero for failure)
- `truncated`: `True` if output was truncated due to size limits

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/9b754bc914cc75c3f6d8c6e99353e81041b73bce/libs/deepagents/deepagents/backends/local_shell.py#L529)
