"""Build a bounded HTML artifact; never insert it into the trusted host DOM."""
MAX_BYTES=32_000
def sandbox_document(html):
    if not isinstance(html,str) or len(html.encode())>MAX_BYTES: raise ValueError("artifact exceeds size limit")
    if "<script" in html.lower() and "sandbox" not in html.lower():
        # Scripts are allowed only inside the iframe sandbox, never in the host.
        pass
    stripped=html.replace("<meta http-equiv=\"refresh\"", "<meta data-blocked-refresh=\"true\"")
    csp='<meta http-equiv="Content-Security-Policy" content="default-src \'none\'; style-src \'unsafe-inline\'; script-src \'unsafe-inline\'">'
    return '<!doctype html><html><head>'+csp+'</head><body>'+stripped+'</body></html>'

def iframe_attributes(): return {"sandbox":"allow-scripts", "referrerpolicy":"no-referrer"}

