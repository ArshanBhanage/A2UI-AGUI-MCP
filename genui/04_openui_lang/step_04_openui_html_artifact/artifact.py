MAX=32000
def html_artifact(source):
    if not isinstance(source,str) or len(source.encode())>MAX: raise ValueError('artifact too large')
    return '<iframe sandbox="allow-scripts" referrerpolicy="no-referrer">'+source.replace('<meta http-equiv="refresh"','<meta data-blocked-refresh="true"')+'</iframe>'
