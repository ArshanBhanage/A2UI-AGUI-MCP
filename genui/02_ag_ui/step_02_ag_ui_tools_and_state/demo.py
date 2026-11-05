from state import apply_patch,authorize_tool
state={'status':'open'}; print('snapshot 0:',state); state=apply_patch(state,{'op':'replace','path':'/status','value':'acknowledged'}); print('snapshot 1:',state); print('tool:',authorize_tool('ack_issue',{'issue_id':'ISS-1'}))
