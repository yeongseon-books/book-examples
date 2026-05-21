"""Generated from book-content article."""

import math


def model(x, w, b):
    return sigmoid(w * x + b)

def sigmoid(z):
    return 1 / (1 + math.exp(-z))
