# 02.1 walkthrough

The server-side lesson creates `RUN_STARTED`, text, and `RUN_FINISHED` events, encodes each as an SSE frame, and rejects unknown event types. AG-UI is transport/state interaction; it does not itself define arbitrary generated HTML.
