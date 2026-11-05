# GenUX codelab rules

This repository implements Assignment 4 as 23 independently runnable lessons.

- Never fabricate live model, host, YouTube, GitHub, deployment, or recording evidence.
- Keep secrets in ignored `.env` files; commit only `.env.example`.
- Label deterministic fixtures as offline examples and live provider checks separately.
- Validate model output before rendering; generated HTML belongs only in a restricted sandbox.
- For each lesson, run unit tests, record evidence, update its README/WALKTHROUGH/DEMO, then update `docs/MILESTONES.md`.

Common commands are documented in the root `Makefile`. Lesson 01.1 is offline-testable without a model key.

