"""Generated from book-content article."""

def evaluate_augmentation(train_base, train_aug, val_loader, train_fn, eval_fn):
    base_model = train_fn(train_base)
    aug_model = train_fn(train_base + train_aug)
    base_metrics = eval_fn(base_model, val_loader)
    aug_metrics = eval_fn(aug_model, val_loader)
    return {
        "base": base_metrics,
        "aug": aug_metrics,
        "delta": {
            key: round(aug_metrics[key] - base_metrics[key], 4)
            for key in base_metrics
        },
    }
