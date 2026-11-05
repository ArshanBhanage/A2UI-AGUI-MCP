from patches import apply
state={'root':'Metric'}; print('revision 0',state); state=apply(state,{'op':'replace','path':'/root','value':'IssueList'}); print('revision 1',state)
