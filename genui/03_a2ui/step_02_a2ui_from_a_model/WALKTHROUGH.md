# 03.2 walkthrough

The agent fixture emits v0.9.1 messages; `correction_loop` validates every envelope and retries boundedly on an invalid result. The invalid-version test demonstrates a failed correction rather than silently accepting a different protocol.
