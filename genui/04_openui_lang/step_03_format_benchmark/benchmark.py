import csv, pathlib
SCENARIOS=['metric','table','chart','form','dashboard','issues','hybrid']
def rows():
    for name in SCENARIOS: yield {'scenario':name,'openui_chars':len(f'Metric(value="{name}")'),'yaml_chars':len(f'value: {name}'),'json_chars':len('{"type":"Metric"}'),'latency':'ESTIMATE_ONLY'}
def main():
    out=pathlib.Path('benchmark.csv'); rs=list(rows())
    with out.open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=list(rs[0])); writer.writeheader(); writer.writerows(rs)
    print('wrote',out,'seven scenarios; latency is estimate-only')
if __name__=='__main__': main()
