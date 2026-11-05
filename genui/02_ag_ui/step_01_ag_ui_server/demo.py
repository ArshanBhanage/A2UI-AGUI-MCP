from events import demo_stream,sse
print('AG-UI educational event stream (offline)')
for item in demo_stream(): print(sse(item),end='')
