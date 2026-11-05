# 01.3 walkthrough

The demo constructs a bounded artifact, injects a `default-src 'none'` CSP, and reports the iframe attributes. Tests cover the CSP, refresh blocking, size limit, and sandbox attribute. The host must not place generated HTML directly into its trusted DOM.

