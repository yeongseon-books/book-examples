"""Generated from book-content article."""

xb, yb = get_batch("train")

for step in range(200):
    optimizer.zero_grad(set_to_none=True)
    _, loss = model(xb, yb)
    loss.backward()
    torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
    optimizer.step()

    if step % 20 == 0:
        print(step, loss.item())
