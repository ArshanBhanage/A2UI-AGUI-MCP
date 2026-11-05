from bridge import harness_to_events
for item in harness_to_events([{'kind':'text','text':'render Metric'},{'kind':'error','message':'no live harness configured'}]): print(item)
