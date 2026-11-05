import base64,json,subprocess
from pathlib import Path
ROOT=Path(__file__).parents[1]
REPO='ArshanBhanage/A2UI-AGUI-MCP'
def api(path,payload):
    p=subprocess.run(['gh','api',path,'--method','POST','--input','-'],input=json.dumps(payload),text=True,capture_output=True,check=True)
    return json.loads(p.stdout)
files=[x for x in subprocess.check_output(['git','ls-files'],cwd=ROOT,text=True).splitlines() if x!='README.md']
entries=[]
for rel in files:
    data=(ROOT/rel).read_bytes()
    blob=api(f'repos/{REPO}/git/blobs',{'content':base64.b64encode(data).decode(),'encoding':'base64'})
    entries.append({'path':rel,'mode':'100644','type':'blob','sha':blob['sha']})
base_commit=subprocess.check_output(['gh','api',f'repos/{REPO}/git/ref/heads/main','--jq','.object.sha'],text=True).strip()
base_tree=subprocess.check_output(['gh','api',f'repos/{REPO}/git/commits/{base_commit}','--jq','.tree.sha'],text=True).strip()
tree=api(f'repos/{REPO}/git/trees',{'base_tree':base_tree,'tree':entries})
commit=api(f'repos/{REPO}/git/commits',{'message':'publish GenUX Assignment 4 codelab suite','tree':tree['sha']})
subprocess.run(['gh','api',f'repos/{REPO}/git/refs/heads/main','--method','PATCH','--input','-'],input=json.dumps({'sha':commit['sha']}),text=True,check=True)
print('published',commit['sha'],'files',len(files))
