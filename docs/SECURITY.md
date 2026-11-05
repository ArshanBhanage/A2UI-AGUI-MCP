# Security notes

Lesson 01.1 treats component names and props as untrusted model output, maps only allowlisted names, escapes text, and renders no model-provided markup. Live provider credentials are server-side only and ignored by Git. Open-ended and hybrid lessons must add iframe sandbox/CSP and message-origin checks before they are considered implemented.

