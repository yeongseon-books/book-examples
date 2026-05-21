"""Generated from book-content article."""

def bayes(p_b_given_a, p_a, p_b_given_not_a, p_not_a):
    p_b = p_b_given_a * p_a + p_b_given_not_a * p_not_a
    return (p_b_given_a * p_a) / p_b

# 질병 유병률 1%, 민감도 95%, 위양성률 5%
result = bayes(0.95, 0.01, 0.05, 0.99)
print(round(result, 4))
