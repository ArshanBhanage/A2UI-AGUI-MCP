from host import classify_host
def test_text_host_is_not_visual(): assert 'text-only' in classify_host('text-client')
def test_visual_host_requires_setup(): assert 'external' in classify_host('Goose')
