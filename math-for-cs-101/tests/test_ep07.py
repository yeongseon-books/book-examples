import numpy as np
from tests.conftest import load_module


def test_ep07_linear_algebra_solution():
    m=load_module('ko/07-linear-algebra/step01_linear_algebra.py')
    x=m.solve_example()
    assert np.allclose(x,[0.2,0.6])
    assert len(m.eigenvalues_example())==2
