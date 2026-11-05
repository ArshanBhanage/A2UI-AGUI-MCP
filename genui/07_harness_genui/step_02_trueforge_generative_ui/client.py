import os,urllib.request
def health():
    url=os.getenv('TRUEFORGE_URL','http://localhost:8790')
    if not url: return {'status':'BLOCKED','reason':'TRUEFORGE_URL is not configured'}
    try:
        with urllib.request.urlopen(url.rstrip('/')+'/api/v1/agents',timeout=3) as response: return {'status':'LIVE','http_status':response.status,'body':response.read().decode()}
    except Exception as exc: return {'status':'BLOCKED','reason':f'{type(exc).__name__}: {exc}'}
