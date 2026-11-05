from benchmark import SCENARIOS,rows
def test_seven_declared_scenarios(): assert len(SCENARIOS)==7 and len(list(rows()))==7
def test_latency_not_measured(): assert all(r['latency']=='ESTIMATE_ONLY' for r in rows())
