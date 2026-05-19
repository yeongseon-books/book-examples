from common import gradient_descent, numerical_derivative
from tests.conftest import load_module


def test_ep08_gradient_descent_near_zero():
    m=load_module('ko/08-calculus/step01_calculus.py')
    assert abs(numerical_derivative(lambda x:x*x,3.0)-6.0)<1e-3
    x=gradient_descent(lambda x:2*x,5.0,lr=0.1,steps=80)
    assert abs(x)<1e-6
    assert abs(m.trapezoid_integral(lambda x:x,0.0,1.0)-0.5)<1e-3
