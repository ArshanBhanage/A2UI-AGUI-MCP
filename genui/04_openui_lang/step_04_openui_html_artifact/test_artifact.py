from artifact import html_artifact
def test_html_artifact_is_boxed(): assert 'sandbox="allow-scripts"' in html_artifact('<h1>custom</h1>')
def test_oversize_rejected():
    try: html_artifact('x'*32001)
    except ValueError: pass
    else: raise AssertionError
