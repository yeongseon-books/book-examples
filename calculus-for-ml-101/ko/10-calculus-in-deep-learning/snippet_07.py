"""Generated from book-content article."""

with torch.no_grad():
    pred = model(x)
    metric = accuracy(pred, y)
