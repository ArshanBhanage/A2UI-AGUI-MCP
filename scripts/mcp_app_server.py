#!/usr/bin/env python3
"""Minimal MCP JSON-RPC stdio server exposing a ui:// issue-triage resource."""
import json, sys

VIEW = """<!doctype html><meta charset='utf-8'><title>Issue triage MCP App</title><style>body{font:16px system-ui;padding:2rem}button{padding:.6rem}</style><h1>Issue triage</h1><p id='count'>Open issues: 12</p><button id='ack'>Acknowledge ISS-1</button><script>document.querySelector('#ack').onclick=()=>parent.postMessage({jsonrpc:'2.0',method:'tools/call',params:{name:'ack_issue',arguments:{issue_id:'ISS-1'}}},'*')</script>"""
def reply(i, result=None, error=None):
    out={'jsonrpc':'2.0','id':i}
    out['error']=error if error else None
    if result is not None: out['result']=result; out.pop('error',None)
    print(json.dumps(out), flush=True)
def main():
    for line in sys.stdin:
        try:
            req=json.loads(line); method=req.get('method'); i=req.get('id')
            if method=='initialize': reply(i,{'protocolVersion':'2025-06-18','capabilities':{'resources':{'subscribe':False},'tools':{}},'serverInfo':{'name':'genux-mcp-app','version':'0.1.0'}})
            elif method=='notifications/initialized': continue
            elif method=='tools/list': reply(i,{'tools':[{'name':'show_issue_triage','description':'Show the issue triage MCP App','inputSchema':{'type':'object','properties':{}} ,'_meta':{'ui':{'resourceUri':'ui://issue-triage/view'}}},{'name':'ack_issue','description':'Acknowledge one issue','inputSchema':{'type':'object','properties':{'issue_id':{'type':'string'}},'required':['issue_id']}}]})
            elif method=='resources/list': reply(i,{'resources':[{'uri':'ui://issue-triage/view','name':'Issue triage view','mimeType':'text/html;profile=mcp-app'}]})
            elif method=='resources/read': reply(i,{'contents':[{'uri':'ui://issue-triage/view','mimeType':'text/html;profile=mcp-app','text':VIEW}]})
            elif method=='tools/call':
                name=req.get('params',{}).get('name'); args=req.get('params',{}).get('arguments',{})
                if name=='show_issue_triage': reply(i,{'content':[{'type':'text','text':'Issue triage view ready'}],'structuredContent':{'issue_count':12},'_meta':{'ui':{'resourceUri':'ui://issue-triage/view'}}})
                elif name=='ack_issue' and args.get('issue_id'): reply(i,{'content':[{'type':'text','text':f"Acknowledged {args['issue_id']}"}]})
                else: reply(i,error={'code':-32602,'message':'unsupported tool or arguments'})
            elif i is not None: reply(i,error={'code':-32601,'message':'method not found'})
        except Exception as exc:
            if 'i' in locals() and i is not None: reply(i,error={'code':-32603,'message':str(exc)})
if __name__=='__main__': main()
