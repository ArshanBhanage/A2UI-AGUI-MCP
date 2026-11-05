# Codex Master Execution Prompt - Assignment 4: GenUX / Generative UI Codelabs

> **READ THIS ENTIRE FILE FIRST. THEN IMPLEMENT, EXECUTE, TEST, RECORD, DOCUMENT AND PUBLISH THE ASSIGNMENT.** This is an execution contract, not a request to write another plan. You are the principal software engineer, technical educator, QA engineer and video-production assistant. Produce one coherent GitHub monorepo containing fully runnable implementations, progressive explanations, real code and execution evidence, recordings, and a submission website. Do not stop after scaffolding. Do not report an unverified integration as working. Follow the milestones in order; finish each milestone's engineering and recording gate before proceeding to the next.

## 0. Assignment statement and interpretation

**Assignment 4 - Demonstrate A2UI, AG-UI, MCP Apps and other GenUX technologies with example code.** Instructor: Vijay Eranti. Worth 500 points. Due **Thursday, November 5, 2026 at 11:59 p.m.**, subject to the LMS course timezone (verify; never infer the submission timezone). Submission type: **one website URL**. The entire set of deliverables must also be in **one GitHub repository**. The instructor requires **step-by-step explanations, complete code walkthroughs, actual execution on video, and a YouTube video for each part**.

Use this exact course reference as the implementation curriculum:
- https://github.com/dlmastery/simple-coding-harness/tree/main/genui
- https://raw.githubusercontent.com/dlmastery/simple-coding-harness/main/genui/README.md
- https://raw.githubusercontent.com/dlmastery/simple-coding-harness/main/genui/WALKTHROUGH.md

The reference course has **23 lessons / 7 themes**. The assignment lists six technology families (A2UI, AG-UI, MCP Apps, json-render, OpenUI, and harness integration). The reference adds **Foundations**, making **7 teaching themes**. Implement all **23 progressively**, not just six landing-page cards or a single generic app. Distinguish **three basic generation modes plus mixed/hybrid**:

1. **Static**: an agent selects from prebuilt, trusted UI components and fills approved props; layout is fixed by the application.
2. **Declarative**: an agent describes layout/structure using a typed, pre-approved catalog or schema; the renderer validates and assembles it.
3. **Open-ended**: an agent produces HTML/CSS/JS or another artifact, isolated in a restrictive sandbox with explicit bridge rules.
4. **Hybrid / mixed**: a trusted catalog-based UI with a bounded, sandboxed generated subregion when needed.

Do **not** confuse generation mode with transport/protocol. **AG-UI** is an agent/frontend event and state interaction protocol; **A2UI**, **OpenUI Lang**, and **json-render** specify/implement UI description and rendering; **MCP Apps** is a protocol extension for placing UI resources in an MCP host; **TrueForge / the harness** is the agent runtime. They can be composed but are not interchangeable. Do not claim that A2UI or AG-UI natively supports arbitrary code or HTML. Show each of the four modes across the teaching suite, and show an actual integration of each mode with each of the six technology families using a documented adapter where necessary. Clearly label native capabilities versus compositions/adapters.

**Video interpretation (stronger than the minimum to eliminate ambiguity):** Record **one separate real instructional MP4 for each of the 23 lessons**, showing the actual source code, execution, interface and verified behavior. Also organize them as **at least 7 YouTube theme entries** (a playlist or an actual compilation per theme is acceptable in addition to the 23 individual uploads). The safest submission is **23 accessible YouTube URLs, organized into 7 themes**, with chapter timestamps for any compilation. A video file, video script, screenshots, or a blank YouTube placeholder alone is NOT equivalent to a published YouTube video. Missing YouTube authentication or user narration is a transparent external blocker, not license to fabricate a link.

## 1. Absolute implementation constraints

1. **Working code only.** No fake running UI, hardcoded tool responses, prerecorded model outputs masquerading as live calls, fake screenshots, invented screenshots, unimplemented buttons, or fabricated execution logs. Never label a scripted offline test as a live agent run. Every live AI flow calls a configured real model; every live remote integration uses a real endpoint and actual credentials. A unavailable upstream service must yield a clear, actionable `BLOCKED` state, not a simulated success.
2. **Static components and deterministic test fixtures are legitimate** when clearly used to teach static rendering, reproduce protocol cases, or unit-test parsers. Do not misunderstand the earlier no-mock rule as prohibiting normal app constants, schema examples, textbook input samples, or test-only fixtures. Keep those in dedicated example/test folders and label them accurately. Never invent business data and display it as live user data. Benchmarks may use carefully specified, reproducible benchmark inputs, explicitly identified as examples rather than external facts.
3. **Actual local .env files.** Create an actual root `.env` and any required per-project `.env` with `KEY=` blank values. Create safe committed `.env.example` files. Ignore ALL `.env` files in Git; do not include credentials in commit history, diagrams, recordings, logs, screenshots, or videos. Provide descriptions for environment variables in READMEs. Never use fake-looking placeholder tokens as if they were functional. Validate config at runtime and explain missing keys.
4. **No AI-slop comments or prose.** No filler praise, magic adjectives, redundant comments explaining trivial operations, fake TODO implementation claims, generic marketing copy, or excessive scaffold. Comments explain important invariants, protocol nuances, security controls, and unusual technical decisions. Clean names, typed interfaces, compact functions, error handling, and precise instructions.
5. **Current APIs, version pinning.** Read primary documentation/source for the chosen package versions before coding; do not blindly paste reference imports. Record actual versions in lockfiles and docs. Use official libraries in the lessons that call for them; do not implement a homemade fake replacement while claiming it is the official protocol. Some codelabs intentionally build a small parser by hand as an educational comparison; label that implementation as custom.
6. **No protocol conflation.** AG-UI event types and lifecycle must be genuine and observable. A2UI payloads must validate against the selected A2UI specification. json-render must use the actual catalog / renderer packages. OpenUI means **OpenUI Lang by `@openuidev/*`**, not `wandb/openui` unless the assignment or reference explicitly distinguishes them. MCP Apps must use the `ui://` resource and permitted host bridge. TrueForge demos must call a real TrueForge runtime/SDK, not print a string that mentions TrueForge.
7. **Security first.** Model-generated HTML must not be inserted into the host DOM as trusted content. Use sandboxed iframes, restrictive CSP, limited privileges and message-type/origin/source checks; never give an untrusted region arbitrary filesystem, network, credentials, host DOM, navigation or unrestricted tool access. Validate schemas and action payloads server-side. No `eval`, arbitrary direct generated JS execution in the main page, unsafe host subprocesses, silent tool approval, uncontrolled external fetches, or insecure public app endpoints. Restrict tools/side effects and seek approval when necessary.
8. **Real evidence.** Executed commands, actual test reports, trace IDs, versions, screenshots, recording metadata, links and failure explanations must be preserved. Mark state explicitly as `NOT_STARTED`, `IN_PROGRESS`, `PASSED`, `BLOCKED`, or `FAILED`. Never say a video was recorded, an integration was tested, a repository was pushed, or a website was deployed without verifying the output.
9. **Single well-structured repository.** Every lesson must have its own runnable folder and `README.md`; every theme must have its own summary README. There must be one top-level index/portal, common tooling and clear navigation. Cite the original course and the licenses of any reused code/assets. Build original cohesive explanations rather than copy-and-paste course text or wholesale source snapshots.
10. **Sequential commits and gates.** For each lesson: implement => unit tests => live integration/real demonstration => screenshots and logs => instructional recording => documented milestone => commit => next lesson. The YouTube publication step can be gated separately after video capture because it requires a user-authorized external account; do not call that separate publication gate passed until actual URLs are verified. Do not force-push or overwrite an unrelated repo.
11. **Academic integrity.** The videos must show work genuinely performed in this new project. Do not generate fabricated terminal sessions or claim an AI-generated voice is the student's own voice. Codex should produce real screen-recorded walkthroughs plus accurately prepared narration (using a transparent TTS voice only if available and allowed); also provide a simple human voice-over replacement workflow. If the grading criteria require the student to personally speak, clearly flag that the student must record/replace narration before final submission.
12. **Fail honestly.** When external authentication, camera/screen permissions, software, account access, deployment billing, or a mandatory live verification is unavailable, document the exact missing dependency and a one-command or specific UI recovery step. Never silently substitute fake output and never mark that feature PASSED.

## 2. First actions: audit the workspace and source

Before writing project code:

- Inspect current directory, Git status, existing project and origin; don't overwrite another assignment. Confirm `python3`, `node`, `npm`/`pnpm`, `git`, `gh`, `ffmpeg`/`ffprobe`, Playwright, screen-recording permissions, GitHub authentication, YouTube OAuth or available browser account, and any model credentials. Do not expose tokens.
- Read the reference `genui/README.md`, every theme README and the specific lesson README before implementing that lesson. Inspect referenced packages and their installed official docs. If browsing/cloning is unavailable, record which original files could not be checked; use verified public docs and do not claim exact replication.
- Read the licensing/attribution requirements of reference repos and dependencies.
- Determine supported Python/Node versions from chosen dependencies; prefer Python 3.12 and a currently supported Node 22+ when compatible with referenced lesson requirements. Pin dependency versions in a Python lockfile and Node lockfile. Use TypeScript for modern frontend packages; Python where the reference uses it. Keep code legible; avoid multi-framework overengineering.
- Prefer a new repository name `genux-protocols-codelab-suite` (or a noncolliding equivalent). If an existing project is provided, preserve it and add folders without destroying the current state.
- Create `docs/IMPLEMENTATION_PLAN.md`, `docs/MILESTONES.md`, `docs/RESEARCH_AND_VERSIONS.md`, `docs/DECISIONS.md`, `docs/SECURITY.md`, `docs/ASSIGNMENT_COVERAGE.md`, `docs/VIDEO_PRODUCTION.md`, and `docs/REFERENCES_AND_LICENSES.md` before implementation.
- Build a verified codelab inventory from the 23 reference lesson READMEs; reconcile broken/outdated commands and note differences in decisions. Do not use relative imports that only happen to work on one machine.
- Create `AGENTS.md` at the root restating the essential project rules, build/test commands, milestone gate and file structure for subsequent Codex sessions.

## 3. Required repository layout

Use the following structure, preserving the exact numbered theme and lesson slugs unless a verified dependency demands a small change. The shape is a contract; content must be real code and actual outputs, not empty folders.

```text
genux-protocols-codelab-suite/
  README.md
  AGENTS.md
  .gitignore
  .env                         # local only, untracked, blank secrets
  .env.example
  Makefile
  pyproject.toml
  uv.lock
  package.json
  pnpm-lock.yaml                # or package-lock.json; pick ONE
  .github/workflows/verify.yml
  site/                         # GitHub Pages submission portal
    README.md
    index.html                  # built output from a real app, not handcrafted fake dashboards
    ...
  genui/
    README.md
    01_foundations/
      README.md
      step_01_static_components/
      step_02_declarative_tree/
      step_03_open_ended_html/
      step_04_hybrid_escape_hatch/
    02_ag_ui/
      README.md
      step_01_ag_ui_server/
      step_02_ag_ui_tools_and_state/
      step_03_ag_ui_from_the_harness/
    03_a2ui/
      README.md
      step_01_a2ui_messages_by_hand/
      step_02_a2ui_from_a_model/
      step_03_a2ui_lit_and_ag_ui/
    04_openui_lang/
      README.md
      step_01_openui_lang_parser/
      step_02_openui_react_lang/
      step_03_format_benchmark/
      step_04_openui_html_artifact/
    05_json_render/
      README.md
      step_01_json_render_catalog/
      step_02_json_render_streaming_patches/
      step_03_json_render_actions_and_targets/
    06_mcp_apps/
      README.md
      step_01_mcp_app_resource/
      step_02_mcp_app_in_a_real_host/
      step_03_mcp_app_hybrid/
    07_harness_genui/
      README.md
      step_01_render_ui_tool/
      step_02_trueforge_generative_ui/
      step_03_trueforge_hybrid/
  packages/
    protocol-core/              # shared schemas, validation, server utilities
    ui-components/              # shared small component catalog, if needed
    demo-runner/                # launch/healthcheck/capture interface
  docs/
    IMPLEMENTATION_PLAN.md
    MILESTONES.md
    RESEARCH_AND_VERSIONS.md
    DECISIONS.md
    SECURITY.md
    ASSIGNMENT_COVERAGE.md
    EXECUTION_GUIDE.md
    VIDEO_PRODUCTION.md
    REFERENCES_AND_LICENSES.md
    benchmarks/
    architecture/
    evidence/
      lesson-01/ ... lesson-23/
  tests/
    README.md
    integration/
    e2e/
    security/
  video/
    README.md
    MANIFEST.md
    YOUTUBE_LINKS.md
    SCRIPTS/
      01_static_components.md ... 23_trueforge_hybrid.md
    CAPTIONS/
    THUMBNAILS/
    PRODUCTION_LOGS/
  recordings/                   # local ignored MP4/WebM masters; do not commit large files
  scripts/
    bootstrap.sh
    check.sh
    run-lesson.sh
    smoke-live.sh
    capture-video.sh
    validate-video.sh
    publish-site.sh
    secrets-scan.sh
  README_SUBMISSION.md
```

Each of the **23 lesson directories** must also contain a `README.md`, `WALKTHROUGH.md`, `DEMO.md`, runnable code, appropriate tests, and real generated evidence files or references. Add `.env.example` in a lesson only if it needs additional configuration. Share common code rather than duplicating a 20-file scaffold 23 times, but keep all 23 independently launchable through a stable command such as `make run LESSON=03.2`. Document the equivalent raw command. A lesson may depend on shared packages, but must not secretly depend on a previous lesson's runtime process.

## 4. Content and example design

Use **one coherent scenario** to show concepts progressing: an **interactive operational dashboard / issue triage assistant**, with actual user-provided input or real public data where a live source is involved. An explanatory data-binding exercise may use explicitly named `sample` inputs; such a sample is not a live integration. Reuse the same concepts (metric card, chart, issue view, action form) to compare generation modes. All live model requests must be transparently labeled live with model/provider, response timestamp, and actual trace results.

Every teaching page must let the grader understand:
- The user's request, agent/model/tool calls, wire-format message, validation step, renderer, visible outcome, and return action.
- Who controls layout, props, allowed actions, UI state, and the boundary separating model output from executable code.
- How the same task differs for static, declarative, open-ended and mixed modes.
- What happens for an invalid schema, invalid tool arguments, interrupted stream, user action, and unavailable model/provider.
- Why the selected technology matters and how it differs from competing ones.

Create a **mode-by-technology coverage matrix** in `docs/ASSIGNMENT_COVERAGE.md`. For all six families, show four practical examples using native support when available or a labeled adapter. A technology page must have four interactive demonstration entries, not merely four paragraphs:

| Family | Static | Declarative | Open-ended | Mixed/hybrid |
|---|---|---|---|---|
| AG-UI | event-delivered known component and values | event stream carries validated UI spec/shared state | AG-UI delivers a pointer to a server-validated sandbox artifact | fixed event-driven cards plus approved sandbox region |
| A2UI | preselected A2UI surface template populated with data | actual A2UI surface and model updates | adjacent sandbox renderer via *explicit external adapter*; **not native A2UI arbitrary code** | A2UI catalog sections plus separately isolated generated region |
| MCP Apps | fixed `ui://` view and genuine tool result | validated dynamic props inside hosted view | model-generated nested sandbox within an MCP App (with CSP) | host view/catalog plus one nested generated artifact |
| json-render | registered fixed card using structured props | real generated catalog spec with validation and patch streaming | separate sandboxed artifact handler, **not a native json-render unchecked JS feature** | json-render catalog plus explicitly sandboxed custom view |
| OpenUI Lang | named trusted component with fixed layout | real line-oriented generated UI program and renderer | `HtmlArtifact` in a sandbox | OpenUI catalog with bounded HTML escape hatch |
| Harness | tool-selected terminal/browser component | real `render_ui` tool with validated spec | tool output mounted only in a restricted external sandbox | catalog and one generated region in complete agent loop |

Where two families share the same cross-mode adapter, reuse tested code and explain the composition. Do not invent compatibility claims. One mode may be demonstrated in an integration subsection of a lesson whose main curriculum centers on another mode, but it must be runnable and discoverable from the UI, README and video.

## 5. Complete 23-codelab implementation syllabus

Each lesson is an independently testable deliverable. Follow the actual upstream lesson README, adapt only where needed for current APIs and security, and cite differences. Mark all steps separately in `docs/MILESTONES.md`.

### Theme 01 - Foundations: four generation modes (4 lessons)

**01.1 `step_01_static_components`:** Implement three trusted frontend components/tools (for example MetricCard, Chart, ActionPanel). Make an authentic agent select a tool/component plus typed values, emit inspectable SSE events, render with fixed application code, and close one safe action loop. Explain why the agent does not generate markup. Verify allowed component mapping and invalid-tool rejection.

**01.2 `step_02_declarative_tree`:** Implement an allowlisted component catalog, actual JSON Schema, dynamic element tree / flat map and incremental JSON stream parser. Validate unknown components and invalid props; display partial rendering, final rendering and error feedback. Compare nested-tree vs flat-element streaming behavior.

**01.3 `step_03_open_ended_html`:** Generate a true HTML artifact with a real model; show editable generated source and render only in a sandboxed iframe. Enforce CSP, `sandbox`, size limits, no implicit network, no host DOM access, strict postMessage schema, and a safe blank/error state. Show an intentional blocked capability so the security boundary is visible.

**01.4 `step_04_hybrid_escape_hatch`:** Use declarative catalog components for standard UI and a `GeneratedView` or equivalent for a narrowly permitted custom visual. Wire button/action to a validated backend action and subsequent agent turn. Show when the agent chooses the catalog and when the escape hatch is justified; test both.

**Theme gate:** All four run separately, static/declarative/open-ended/hybrid interactions are live (or missing credentials transparently blocked), at least one test per security boundary, all four walk-through recordings are real and decodable, four lesson READMEs and a theme README are complete. Commit verified work.

### Theme 02 - AG-UI: event-based agent/frontend transport (3 lessons)

**02.1 `step_01_ag_ui_server`:** Implement a real AG-UI endpoint: run start, text streaming, run finish/error, well-formed SSE framing, event IDs where applicable and a browser client that consumes it. Use the official AG-UI event schema/client when supported; explain any hand-written educational layer and test wire compatibility. Verify disconnect handling.

**02.2 `step_02_ag_ui_tools_and_state`:** Stream real tool-call lifecycle events and maintain shared UI state via snapshots and JSON Patch deltas. Give a client-side tool an explicit allowlist and lifecycle. Show state evolution and reject invalid deltas/actions. Explain why the event stream is distinct from the UI description format.

**02.3 `step_03_ag_ui_from_the_harness`:** Bridge actual coding-agent harness callbacks to AG-UI; use the official AG-UI client where available. Show a real tool call, streaming UI update and final state. Add visible static, catalog, sandbox and hybrid surfaces as *AG-UI-delivered experiences*, not purported new native AG-UI modes.

**Theme gate:** Event traces, actual UI/state transitions, failure-recovery test, security check, three instructional videos, and a comparison table of AG-UI vs A2UI vs MCP Apps. Commit.

### Theme 03 - A2UI: agent-described UI surfaces (3 lessons)

**03.1 `step_01_a2ui_messages_by_hand`:** Select and **pin one real A2UI specification**. The currently documented v0.9.1 is the production release; v1.0 is a candidate, so do not mix message shapes across versions. Build and validate `createSurface`, `updateComponents`, `updateDataModel` and the correctly specified final/remove message for the pinned version. Render a real surface; show structure/data separation and invalid message handling. Read actual schemas; never infer envelope fields from an older tutorial.

**03.2 `step_02_a2ui_from_a_model`:** Generate A2UI messages from a real LLM/agent using a typed catalog and structured instruction, stream and validate incrementally, feed structured validation errors back through a bounded correction loop, and handle safe user actions. Distinguish streamed partial UI from complete validated UI. Record traces of actual model generation.

**03.3 `step_03_a2ui_lit_and_ag_ui`:** Integrate an official supported A2UI renderer (Lit or current official React renderer) with A2UI messages carried through AG-UI events. Demonstrate distinct representation and transport boundaries, UI actions and response messages. Complete the A2UI four-mode comparison via explicit external adapter for open-ended content, without allowing arbitrary code through the catalog.

**Theme gate:** Three A2UI validations, one official renderer working, A2UI version documented, action round-trip, real streaming demonstration, three recorded code/execution videos, README/evidence. Commit.

### Theme 04 - OpenUI Lang: line-oriented format and hybrid artifacts (4 lessons)

**04.1 `step_01_openui_lang_parser`:** Educational parser for line-oriented `id = Component(args)` statements with typed arguments, references that may point forward, incremental parsing, error recovery and a hand-built DOM renderer. Include Python and JavaScript parsing tests where useful. Label custom parser as custom.

**04.2 `step_02_openui_react_lang`:** Use current official `@openuidev/lang-core` and `@openuidev/react-lang` packages. Define a Zod catalog with `defineComponent` and a `createLibrary` where documented; generate a catalog-aware system prompt with the package's current API, stream genuine OpenUI Lang output over SSE and render in React. Do not substitute the unrelated W&B OpenUI repository.

**04.3 `step_03_format_benchmark`:** Implement a reproducible comparison for **seven declared scenarios** across OpenUI Lang, YAML, C1 JSON when available from documented definitions, and json-render's element map. Produce exact input formats, tokenizer name/version (`o200k_base` if verified), generated files, script, reproducible token counts, output CSV and plots. Clearly separate **measured token counts** from **estimated generation latency** (e.g., a declared tokens/second estimate), never claim estimated speed is a measured end-to-end benchmark. Do not force a preselected winner or copy numbers from a report without reproduction.

**04.4 `step_04_openui_html_artifact`:** Use trusted OpenUI components, `Markdown` when supported, and a bounded `HtmlArtifact` escape hatch. Capture streaming source before render, validate artifact size/type, run in a CSP-enforced sandbox and demonstrate a catalog-only dashboard versus a custom interactive artifact. Add actionable security tests.

**Theme gate:** Four complete codelabs, parser-vs-library explanation, real format benchmarks, actual React streaming, four instructional recordings, traceable README/evidence. Commit.

### Theme 05 - json-render: catalog, patches and multiple targets (3 lessons)

**05.1 `step_01_json_render_catalog`:** Use current official `@json-render/core` and `@json-render/react`, define an actual component/action catalog, produce a model prompt via library-supported API, validate a generated spec, render it with real components and reject unknown types/props.

**05.2 `step_02_json_render_streaming_patches`:** Stream validated RFC 6902 JSON Patch updates to a real element map; apply them in UI, track ordered revisions and handle patch failures without corrupting the last valid state. Measure actual time to first usable render and final render using `performance` or trace timestamps. Describe methodology and report only real measured results.

**05.3 `step_03_json_render_actions_and_targets`:** Add action handler confirmation/authorization, tool round-trip and at least two real render targets (React/browser and terminal via a supported renderer or a transparently labeled adapter). Show spec portability and differences in interaction. Demonstrate static, declarative, external-sandbox open-ended, and mixed patterns without claiming generated JS is part of json-render's native catalog.

**Theme gate:** Three codelabs, end-to-end patch/action UI and two target renderers, security/schema tests, screenshots, three actual videos. Commit.

### Theme 06 - MCP Apps: UI resources in an external host (3 lessons)

**06.1 `step_01_mcp_app_resource`:** Build a real MCP server/tool exposing an MCP Apps `ui://` resource, tool metadata linking the view and the tool, and a sandboxed HTML view. Implement a minimal conformant host or use an official host SDK. Ensure the declared `ui://` resource, tool result / structured data and JSON-RPC bridge are real. Validate allowed actions and message source. Use current `modelcontextprotocol/ext-apps` specification, not an unrelated ad-hoc iframe contract marketed as MCP Apps.

**06.2 `step_02_mcp_app_in_a_real_host`:** Connect the same MCP server to an actual MCP host that supports MCP Apps. Provide setup docs for relevant hosts, but **test a visual-capable host** and distinguish it from a text-only MCP client. If an external host's UI extension is not supported or the account is not connected, document exactly what is blocked; don't claim an iframe rendered. Explain why a standard MCP tool response alone does not prove MCP App UI integration.

**06.3 `step_03_mcp_app_hybrid`:** Extend a real hosted MCP App with a trusted catalog and one model-generated nested HTML artifact. Enforce both the host iframe and the inner sandbox; keep model credentials on the backend. Demonstrate message routing, user actions, updates and safe rejection of an illegal operation. Label four modes in the MCP Apps interface.

**Theme gate:** Three lessons, actual `ui://` resource and host bridge, one host integration observed, two-level sandbox security tests, real videos, README/evidence. Commit.

### Theme 07 - harness integration: the complete agent loop (3 lessons)

**07.1 `step_01_render_ui_tool`:** Integrate a genuine validated `render_ui(spec)` tool into a coding-agent loop. Render the same spec in terminal (e.g. Rich) and a web page (e.g. SSE). Show tool selection, argument validation, action/response and error handling. This must execute the tool, not just show source snippets.

**07.2 `step_02_trueforge_generative_ui`:** Use an actual TrueForge local or hosted server and its documented SDK. Enable the runtime's generative UI capability where supported; capture, parse and render genuine streamed OpenUI Lang output in the project's page. Show session creation, model turn, tool/stream trace and visibly updated page. If TrueForge access is unavailable, mark the integration blocked; do not replace it with a custom print statement.

**07.3 `step_03_trueforge_hybrid`:** Add an explicitly approved `HtmlArtifact` custom region alongside trusted catalog components to the TrueForge-driven browser UI. Show two real requests: one handled by the catalog, one requiring a safe custom artifact. Test sandbox, invalid artifact rejection, stream failure recovery and action boundaries. Explain that a custom browser adapter does not automatically change the hosted TrueForge chat UI.

**Theme gate:** Three working harness examples, actual SDK communication, browser + terminal rendering, security checks, three real narrated execution recordings, theme README and evidence. Commit.

## 6. Mandatory lesson documentation and tutorial quality

Every `genui/<theme>/<lesson>/README.md` must follow this order:

1. **What this lesson demonstrates** in precise technical terms.
2. **Prerequisites / supported versions** and source reference.
3. **Architecture diagram and trust boundary** with real components and event/data paths.
4. **Learning objectives** and an explanation of how it follows the previous lesson.
5. **Configuration**: `.env` variables and provider setup, no secrets in Git.
6. **One-command quick start** and its equivalent explicit shell commands.
7. **Source walkthrough**, by actual file/function names and what they do.
8. **Wire-format / schema illustration** derived from validated local examples; no fictitious live run claims.
9. **Execution walkthrough**: exact inputs, UI actions, terminal commands, expected classes of responses, and real output observations with evidence links.
10. **Tests, validation and failure cases**, including real commands and observed outcome.
11. **Static / declarative / open-ended / hybrid context**, showing which this lesson natively teaches and links to its integrations.
12. **Security and limitations** with real caveats.
13. **YouTube link** (actual verified URL when published; else `NOT PUBLISHED - see video/MANIFEST.md`) and **local recording** proof.
14. **Next lesson** link.

Each `WALKTHROUGH.md` is a spoken-style but technical code walkthrough: file overview, command, what was executed, actual event/message response and why, test behavior, and pitfalls. Each `DEMO.md` contains literal test inputs (allowed) and actual observed results/logs/capture filenames; no invented run successes. The theme README must introduce the key concept, chart the lesson progression, link all videos, and compare behavior across the four modes. The root README must cover the whole 23-lesson curriculum and easy navigation.

Every meaningful source code snippet in a README must either be checked against its actual file with a snippet checker or replaced with a link to the exact file/range. Do not let documentation rot from the code. Prefer architecture/sequence Mermaid diagrams where they improve comprehension, but never fabricate deployment diagrams.

## 7. Real VIDEO production: non-optional deliverable for EVERY codelab

### 7.1 Required video count and output

**Make 23 separate recordings**, one per numbered lesson. Do not stop at creating `VIDEO.md` placeholders. Default format: `.mp4`, H.264 video + AAC audio, 1920x1080 (or 1280x720 if resources require), readable font, 16:9, accessible captions. Aim for a focused ~3-7 minute lesson where practical; use the actual complexity, do not artificially accelerate code to unreadable speed. Each one must show:

1. Title card with **specific lesson name, technology, mode** (brief; not a substitute for a demo).
2. Open the actual repository and show exact source file/function(s) while explaining their role.
3. Show real commands being executed (terminal, IDE terminal, or screen recording) and version/config check **with all secrets redacted**.
4. Show the live application running in a browser, terminal or real MCP host, including actual user input, output, event stream/tool calls and a user action if applicable.
5. Show one real test run and its actual pass/fail status; don't claim hidden/skipped tests passed.
6. Show a relevant failure/security/validation case where this is part of the lesson.
7. Explain static/declarative/open-ended/hybrid classification and the protocol/transport distinction.
8. End with a clear, accurate conclusion and next lesson.

**One video per theme is NOT enough unless it contains complete walkthrough coverage for each lesson in that theme.** Produce 23 individual videos first, then (if possible) make 7 compilation/playlists for convenient grading. Each must have a unique slug and metadata in `video/MANIFEST.md`. Provide a practical, truthful YouTube publication plan for both sets.

### 7.2 Codex must actually capture real footage

- At the beginning of each lesson, inspect recording tooling. Prefer an actual full-screen capture via available OBS, macOS screen-recording tool, or `ffmpeg` capture with permission. If a desktop capture is impossible in a headless environment, use **real Playwright browser video** (not synthetic screenshots) combined with a **real terminal session recording** via `asciinema`, with commands and timestamps. Assemble both captures into an actual video with ffmpeg; don't simulate terminal content.
- Automation must capture the REAL executed application with actual network events and corresponding server logs, not a static mockup. Use Playwright to drive truthful interactions. Programmatically blur/redact secrets and user identifiers before publishing; ensure no auth cookies, keys or personal file paths appear.
- Generate a **lesson-specific narrative script** in `video/SCRIPTS/<lesson>.md`, with explicit code references, commands, visible observations, and explanation of why the chosen architecture works. Use actual transcript from captured execution where helpful.
- **Audio is required.** If a permitted offline/system TTS engine is available, produce transparent **synthetic narration** from the accurate script and include it in the video; never claim it is the student's own voice. If only the user's own recorded voice fulfills the course standard, deliver the real screen capture, captions and a timed script plus a documented voiceover replacement command, and mark `STUDENT_VOICE_REQUIRED` until replaced. Do not generate an unapproved voice clone or impersonate the student.
- Produce matching `.srt` or `.vtt` captions from the actual narration script and review timing. Ensure text/code on screen remains legible.
- Use `ffprobe` to verify actual video duration, width/height, codecs and **a nonempty audio stream**. Check that capture is not 100% black, missing the running application, or only a slideshow. Inspect opening/middle/end representative frames. Save result and SHA-256 in `video/PRODUCTION_LOGS/<lesson>.md`.
- If recording is technically blocked, mark `BLOCKED: SCREEN_RECORDING_PERMISSION` or the actual blocker, and stop claiming the milestone passed. A fake video generated from sample HTML or recreated terminal logs is strictly forbidden.
- Do not commit large video binaries to normal Git history. Store recordings locally in ignored `recordings/`. Publish via YouTube after authenticated approval; optionally upload masters as GitHub release assets or Git LFS if configured. Commit the script, captions, thumbnails, technical video manifest and verified accessible YouTube URLs.

### 7.3 Exact video manifest contract

`video/MANIFEST.md` must track **all 23 numbered lessons** with:

`lesson_id | theme | title | actual_mp4_path | source_code_commit | capture_status | runtime_verified | ffprobe_duration | audio_verified | caption_path | voice_type (student / clearly-labeled TTS) | youtube_url | youtube_status | evidence_path | error_or_blocker`

Statuses allowed: `NOT_STARTED`, `CAPTURED`, `VALIDATED`, `UPLOADED`, `BLOCKED`, `FAILED`. No pre-filled working URLs, durations, test passes or capture statuses. Keep `video/YOUTUBE_LINKS.md` as a generated index populated **only after** YouTube confirms the real video ID and the URL resolves. Every lesson README and the GitHub Pages website must link the actual lesson video only after publishing.

### 7.4 YouTube upload is required, but never fake it

- Check whether the user has an authenticated YouTube account or explicitly configured OAuth client and upload permissions. **Never ask the user to paste an access token in chat or record it on screen.** If there is a supported authenticated browser or YouTube Data API flow, use that flow only with permission and least-privileged scopes; upload each video as unlisted or public according to the user's instructions. Prefer **unlisted but accessible via link** for grading, not private inaccessible videos. Use genuine titles, ordered descriptions, source repo link, chapter links and captions.
- If YouTube OAuth/permissions are missing, prepare all 23 validated files, titles/descriptions/captions and a repeatable upload process, then stop the publishing milestone with a precise user action required. **Do not say the YouTube requirement is complete until actual URLs resolve.** A URL placeholder, fake YouTube ID or GitHub-hosted MP4 alone does not pass the YouTube publication gate.
- Check with the user if grading requires **the student's own voice**. Produce accurate recording assets regardless; label TTS honestly and make replacing narration straightforward. Never declare that automatically narrated footage satisfies a requirement to *personally explain* without confirmation.

## 8. GitHub Pages website and submission experience

The LMS asks for a website URL, not a ZIP file. Build and deploy an actual **GitHub Pages submission portal** linked to the monorepo. The site must work as a static page without exposing private API keys; do not pass model credentials into static browser JavaScript. The portal is an **index and verifiable demo/documentation hub**, not a fake remote backend.

Required sections:
- Course title, assignment brief, author identity only if user supplies it, due date, repository link.
- Seven themes, ordered 23 lesson cards, each with a concise objective, mode, source link, README, walkthrough, real screenshot, test evidence and YouTube URL (when verified).
- A six-technology-by-four-mode coverage comparison; label native versus composed adapters.
- A clear diagram explaining transport versus UI description versus harness.
- Video library / YouTube playlists, captions links, and recording-verification status.
- A quickstart/how to reproduce locally, required provider credentials, known limitations and security notes.
- A tests/coverage summary derived from actual results; no fake 100% badges.
- A final submission link that is actually accessible outside localhost (GitHub Pages or other real site). Confirm its HTTP status and check the site as a logged-out user where possible.

If GitHub Pages publishing is blocked by account/org restrictions, document the exact blocker. The public GitHub repository URL is an acceptable **fallback candidate** for website URL submission only after explicitly confirming the LMS accepts repository URLs; do not assume this is equivalent to a deployed site.

## 9. Quality assurance, evals and security tests

Use a simple, reproducible commands contract such as:

```bash
make bootstrap                  # installs pinned deps, checks required tools
make lint
make typecheck
make test                       # unit tests, no external dependency required
make integration                # real endpoints only; honest skips and blockers
make e2e                        # actual browser/host execution
make security                   # CSP, tool allowlist, path traversal, injection checks
make docs-check                 # validates links, snippets, 23 README contracts
make run LESSON=01.1           # launches one lesson
make demo LESSON=01.1          # runs real example; model call if configured
make video LESSON=01.1         # real recording + verification, no simulations
make video-verify LESSON=01.1
make site                      # build submission portal
make verify                    # combined gate; never count blocked as passed
```

Implement these targets in the repo (minor command differences are allowed if clearly documented). Unit tests may use deterministic fixtures, restricted to tests; integration/E2E tests must exercise real code paths. Mark tests requiring live providers with an explicit `LIVE` marker; no fabricated pass when they are skipped. Use Playwright tests for actual UI actions, SSE states, errors and sandbox isolation. Test malformed JSON, unknown components, bad patches, invalid A2UI envelopes, unauthorized MCP bridge calls, incorrect AG-UI event ordering, failed model call, interrupted streams, no tool approval, CSP violations, and sanitizer/secret checks.

Verify that `.env` files are absent from tracked Git paths (`git ls-files`), tracked history is secret-free (appropriate available scanner), and built frontend bundles have no provider secrets. Run reproducible benchmark scripts and label any estimation separately from measurements.

The `docs/evidence/lesson-NN/` directory must hold **actual** sanitized logs or traces, run metadata, command results, screenshots, test evidence and video verification reports; do not commit sensitive raw traces. Every claimed result must point to a file and a command that reproduces it.

## 10. Milestones and strict acceptance gates

Create exactly these progress groups in `docs/MILESTONES.md`, with subrows for all 23 lessons and their captures. Each group includes goals, implementation checklist, exact commands, blockers, test evidence, video path and Git SHA. Do not skip ahead; record progress in files so subsequent Codex sessions can resume without losing context.

| ID | Milestone | Exit gate |
|---|---|---|
| M0 | Preflight, source research, tech decisions, repo scaffold | Current APIs researched, 23 lesson map, `.env` + gitignore, build commands, clean initial commit |
| M1 | Foundations lessons 01.1-01.4 | 4 working lessons, 4 tests/trace sets, 4 real validated MP4s, docs + commit |
| M2 | AG-UI lessons 02.1-02.3 | 3 verified event/state flows, 3 real validated MP4s, docs + commit |
| M3 | A2UI lessons 03.1-03.3 | 3 valid A2UI flows, official renderer, 3 real validated MP4s, docs + commit |
| M4 | OpenUI lessons 04.1-04.4 | 4 working lessons, real benchmark, 4 real validated MP4s, docs + commit |
| M5 | json-render lessons 05.1-05.3 | 3 real spec/stream/action demos, 3 validated MP4s, docs + commit |
| M6 | MCP Apps lessons 06.1-06.3 | 3 MCP demos, actual host integration evidence, 3 MP4s, docs + commit |
| M7 | Harness lessons 07.1-07.3 | 3 complete loop demos, actual TrueForge integration, 3 MP4s, docs + commit |
| M8 | Cross-mode/technology coverage | 6x4 demos documented and runnable; native vs adapter labels; security/e2e checks pass |
| M9 | Video publishing | 23 recordings + audio + captions validated, accessible YouTube links verified or external blocker clearly identified; 7 themed indexes/playlists |
| M10 | Website, final QA and deployment | GitHub Pages works publicly, 23 docs links resolve, actual checks/evidence, source+site linked |
| M11 | GitHub publication and submission audit | All intended commits pushed, public repo/site verified, complete accurate submission report |

**Gate invariant:** Do not begin M2 until M1's **four recordings exist and were verified**, and likewise for subsequent theme stages. YouTube uploading is an external-account-dependent publication gate at M9, not a reason to falsify earlier codelab recordings. If M9 is blocked, report the missing access prominently and **do not claim the assignment is fully submitted**. Similarly, do not mark a theme's live integration as PASSED when a necessary credential was missing. You may perform local implementation work on unaffected codelabs after documenting a live-provider blocker, but retain its blocked status and do not present milestone gates as passed.

Each individual codelab must have an internal submilestone sequence:

1. `Lx-A`: researched spec and source, documented diagram and exact dependency versions.
2. `Lx-B`: implemented actual source and created local configuration.
3. `Lx-C`: passed static/type/unit checks; integration verified or precisely blocked.
4. `Lx-D`: real UI/terminal execution observed; captured logs/screenshot.
5. `Lx-E`: actual screen/video recording captured, narrated or marked student voice required, ffprobe verified; script/captions in repo.
6. `Lx-F`: README, WALKTHROUGH, DEMO and manifest entry correct; committed.

A failed phase must be fixed and rerun, not bypassed by writing a passing status. Do not manufacture evidence. Never automatically spend money or provision chargeable cloud infrastructure without understanding costs and user permission.

## 11. Source-of-truth references to use

Verify current versions and syntax in **official sources**, rather than treating historical code as infallible:

- The exact curriculum: https://github.com/dlmastery/simple-coding-harness/tree/main/genui
- Raw curriculum README: https://raw.githubusercontent.com/dlmastery/simple-coding-harness/main/genui/README.md
- Reference walkthrough: https://raw.githubusercontent.com/dlmastery/simple-coding-harness/main/genui/WALKTHROUGH.md
- AG-UI: https://github.com/ag-ui-protocol/ag-ui and https://docs.ag-ui.com/
- A2UI: https://github.com/a2ui-project/a2ui and https://a2ui.org/
- A2UI specification versions: https://github.com/a2ui-project/a2ui/tree/main/specification
- MCP Apps official extension: https://github.com/modelcontextprotocol/ext-apps and https://modelcontextprotocol.io/extensions/apps/overview
- json-render: https://github.com/vercel-labs/json-render
- OpenUI Lang docs: https://www.openui.com/docs/api-reference/react-lang and https://www.openui.com/docs/build-agents/ui-generation
- TrueForge runtime: https://github.com/truefoundry/trueforge
- OpenUI State of Generative UI report for benchmark context: https://www.openui.com/blog/state-of-generative-ui-report
- Video tooling (select what's installed): FFmpeg, ffprobe, Playwright and an actual screen-recording/terminal-recording utility.

The original curriculum's actual lesson numbering and the differentiation between custom educational parsers versus official package implementations should remain visible in the README and source annotations. Honor source licenses when reusing any implementation. The curriculum's original recorded outputs do **not** count as this project's execution evidence.

## 12. Deliverables checklist - what must be real at the end

- [ ] One public or grader-accessible GitHub monorepo, clean history and all required code.
- [ ] One submitted/accessible website URL with links to source, tutorial evidence and videos.
- [ ] 7 theme READMEs and **23 codelab READMEs, walkthroughs and demo instructions**.
- [ ] **23 progressively executable lessons**, each with source, tests, real execution and captured proof.
- [ ] **6 technologies x 4 modes** visibly and accurately covered, native vs composed distinctions documented.
- [ ] Current primary APIs used, version pinning, security controls and actionable config.
- [ ] Root and needed local actual `.env` files with blank values; `.env.example` committed, secrets excluded.
- [ ] No fake data or mock application behavior in live demonstrations; deterministic test/example inputs clearly labeled.
- [ ] **23 genuine lesson-specific MP4 recordings**, checked with ffprobe and reviewed for code legibility and live execution.
- [ ] **23 complete video scripts and captions**, audio verified or accurately flagged for student voice replacement.
- [ ] **23 accessible, real YouTube URLs**, 7 organized theme video indexes/playlists, or a conspicuous documented external OAuth/human narration blocker. Do not claim full completion if missing.
- [ ] Real GitHub Pages site deployed and checked (unless expressly blocked).
- [ ] Tested commands, honest metrics and live run evidence in `docs/evidence`.
- [ ] GitHub push verified (`git status`, `git log`, `git remote -v`, `gh repo view` where authenticated); no token exposure.
- [ ] `README_SUBMISSION.md` with actual website URL, repository URL, 7-theme navigation, 23 YouTube links, blockers and exact verification summary.

## 13. Final status report to the user

Do not finish with a generic "All done". Return a concise, verifiable summary:

- GitHub repo URL, exact commit SHA, repository visibility.
- Public website URL and observed availability.
- 23/23 implementation/test/demo counts, with any blocked case distinguished from passed.
- 23/23 video capture/audio/caption counts and 23 YouTube URLs or precisely enumerated missing uploads; 7 theme group links.
- Static/declarative/open-ended/hybrid matrix completion with native-versus-adapter caveats.
- Security/secret scan result, CI status and actual commands executed.
- Any user-only steps (YouTube login/permissions, spoken narration, provider keys, publishing authorization), with exact paths/commands needed. Never imply Codex can authenticate or publish to an account it cannot access.

**START NOW:** Inspect the workspace and official curriculum, create M0 plan/files, initialize a clean repository, and implement lesson 01.1. Execute its tests, run the live demo, generate and verify its real instructional video, commit it, then continue lesson by lesson using the gate procedure. Do not rewrite this prompt as an alternative plan and stop.
