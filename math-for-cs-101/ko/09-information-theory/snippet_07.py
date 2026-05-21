"""Generated from book-content article."""

def information_gain(parent_h: float, left_h: float, right_h: float, left_ratio: float, right_ratio: float) -> float:
    child_h = left_ratio * left_h + right_ratio * right_h
    return parent_h - child_h
