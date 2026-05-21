# y_hat = XW, L = mean((y_hat - y)^2)

pred = X @ w_hat
err = pred - y
grad = 2 * X.T @ err / len(y)
print('grad shape:', grad.shape)
