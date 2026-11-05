# 01.1 production verification

- Capture method: Playwright 1.60.0 with Chromium 148, recording the real local FastAPI application.
- Footage includes actual `catalog.py` source, actual pytest output, and an actual browser interaction against `/api/run`.
- Demo mode: OFFLINE FIXTURE. It is not a live model run.
- Output: `recordings/lesson-01-1-static-components.mp4` (local ignored artifact).
- ffprobe: H.264 video, AAC audio, 1280x720, 8.96 seconds, 224 decoded frames.
- SHA-256: `8a39e21504a12c1a734f6d80c6c8e4fc71dbc7a539b0c730f8b4f48f80b7d7e7`.
- Captions: `video/CAPTIONS/01_static_components.srt`.
- Voice: clearly labeled synthetic macOS TTS; replace with student narration if required by the course.
- Representative frame review: title/source/test/application footage present; no black-only output observed.
- YouTube: not uploaded; user will perform upload.

## Additional complete demo

- Output: `recordings/demo-lesson-01-1-static-components.mp4`.
- Purpose: demo-only capture, separate from the compact walkthrough.
- ffprobe: H.264 video, AAC audio, 1280x720, 34.04 seconds.
- SHA-256: `35cb1beb43c6324300f8c2eab9a065baf0bd79e5cbaaefa89b4f483ef2c857b1`.
- Final-frame review shows an explicit `Demo complete` card with the offline-fixture disclosure.
