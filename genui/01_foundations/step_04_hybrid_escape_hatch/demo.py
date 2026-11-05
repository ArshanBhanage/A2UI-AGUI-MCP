from hybrid import choose_surface
print('mode: HYBRID')
print(choose_surface('Metric',{'title':'Open issues','value':'12'}))
print('sandboxed custom bytes:', len(choose_surface('GeneratedView',{'html':'<h1>Custom visual</h1>'})['artifact']))

