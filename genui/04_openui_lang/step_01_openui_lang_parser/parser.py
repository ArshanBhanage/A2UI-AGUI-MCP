import re
CALL=re.compile(r'^([A-Za-z_]\w*)\((.*)\)$')
def parse_line(line):
    left,right=line.split('=',1); m=CALL.match(right.strip())
    if not m: raise ValueError('invalid OpenUI Lang statement')
    args=[x.strip().strip('"') for x in m.group(2).split(',') if x.strip()]
    return {'id':left.strip(),'component':m.group(1),'args':args}
def parse(program): return [parse_line(x.strip()) for x in program.splitlines() if x.strip()]
