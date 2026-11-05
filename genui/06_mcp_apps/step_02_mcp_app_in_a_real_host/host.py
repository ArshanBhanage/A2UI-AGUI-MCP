def classify_host(name):
    if name in {'Claude Desktop','Goose'}: return 'visual-capable host requires external setup'
    if name=='text-client': return 'text-only; does not prove MCP App UI'
    return 'unknown host'
