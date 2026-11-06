# GenUX Protocols Codelab Suite

Assignment 4 implementation workspace for 23 generative-UI lessons across seven themes. The curriculum distinguishes generation mode (static, declarative, open-ended, hybrid) from transport or host protocols (AG-UI, MCP Apps) and from UI description formats (A2UI, OpenUI Lang, json-render).

## Status

M0 is in progress. Lesson 01.1 has an offline implementation and tests. Live model execution, screen recording, YouTube publication, GitHub publication, and deployment remain unverified until their required credentials and permissions are available.

## Navigation

- [Assignment coverage](docs/ASSIGNMENT_COVERAGE.md)
- [Milestones](docs/MILESTONES.md)
- [Research and versions](docs/RESEARCH_AND_VERSIONS.md)
- [Lesson 01.1: static components](genui/01_foundations/step_01_static_components/README.md)
- [Submission report](README_SUBMISSION.md)

The source curriculum is [simple-coding-harness/genui](https://github.com/dlmastery/simple-coding-harness/tree/main/genui). Its README and walkthrough were checked on 2026-11-04; historical screenshots and outputs are not treated as local evidence.

## Current deliverables

All 23 numbered lesson folders are present with runnable demos, tests, and lesson documentation. Use `make test` to run each lesson's tests in isolation. The local TrueForge smoke test uses `npx @truefoundry/trueforge`; the MCP Apps example uses the configured local stdio server in `scripts/mcp_app_server.py`.

The lesson recordings are local ignored artifacts under `recordings/`. Their technical status is tracked in [`video/MANIFEST.md`](video/MANIFEST.md). YouTube URLs are intentionally placeholders in [`video/YOUTUBE_LINKS.md`](video/YOUTUBE_LINKS.md) until the videos are uploaded.

## Publishing

Target repository: [ArshanBhanage/A2UI-AGUI-MCP](https://github.com/ArshanBhanage/A2UI-AGUI-MCP). After authenticating with `gh auth login` or `gh auth setup-git`, publish the local branch with:

```bash
git fetch origin main
git merge origin/main --allow-unrelated-histories -X ours -m "merge GitHub seed"
git push -u origin main
```

