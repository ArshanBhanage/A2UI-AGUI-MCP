import os,urllib.request
def health():
    url=os.getenv('TRUEFORGE_URL')
    if not url: return {'status':'BLOCKED','reason':'TRUEFORGE_URL is not configured'}
    try:
        with urllib.request.urlopen(url.rstrip('/')+'/health',timeout=3) as response: return {'status':'LIVE','http_status':response.status}
    except Exception as exc: return {'status':'BLOCKED','reason':f'{type(exc).__name__}: {exc}'}
