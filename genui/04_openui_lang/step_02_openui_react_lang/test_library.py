from library import prompt,official_package_status
def test_catalog_prompt(): assert 'Metric' in prompt() and 'IssueList' in prompt()
def test_blocker_is_explicit(): assert official_package_status().startswith('BLOCKED')
