from conftest import load_episode

def test_09_performance_optimization():
    mod=load_episode('ko','09-performance-optimization.py')
    res=mod['run_demo']()
    assert res["uses_index"] and abs(res["col_sum"]-res["base_sum"])<0.01
