"""Generated from book-content article."""

def information_gain(parent_entropy, left_weight, left_entropy, right_weight, right_entropy):
    child_entropy = left_weight * left_entropy + right_weight * right_entropy
    return parent_entropy - child_entropy

print(information_gain(1.0, 0.4, 0.0, 0.6, 0.9183))
