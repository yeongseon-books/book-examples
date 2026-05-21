"""Generated from book-content article."""

def bayes_posterior(p_pos_given_disease: float, p_disease: float, p_pos: float) -> float:
    return (p_pos_given_disease * p_disease) / p_pos

# 예시 수치
p_disease = 0.01
p_pos_given_disease = 0.95
p_pos_given_healthy = 0.10
p_pos = p_pos_given_disease * p_disease + p_pos_given_healthy * (1 - p_disease)
posterior = bayes_posterior(p_pos_given_disease, p_disease, p_pos)
