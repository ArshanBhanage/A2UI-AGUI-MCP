from sandbox import sandbox_document, iframe_attributes
artifact='<style>body{font:24px system-ui;background:#101827;color:white}</style><h1>Generated issue view</h1><button>Refresh</button>'
print('mode: OPEN-ENDED OFFLINE ARTIFACT')
print('iframe boundary:', iframe_attributes())
print('CSP artifact bytes:', len(sandbox_document(artifact).encode()))

