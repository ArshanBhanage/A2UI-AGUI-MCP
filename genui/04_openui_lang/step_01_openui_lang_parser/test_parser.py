from parser import parse
def test_line_parser(): assert parse('title = Text("Open issues")')[0]['component']=='Text'
def test_forward_lines(): assert len(parse('root = Column(title)\ntitle = Text("Open")'))==2
def test_invalid_statement():
    try: parse('bad')
    except ValueError: pass
    else: raise AssertionError
