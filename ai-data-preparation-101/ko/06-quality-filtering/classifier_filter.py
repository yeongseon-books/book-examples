# pip install fasttext
import fasttext

# 1) Prepare training data: wiki/books as positive, common-crawl junk as negative
# format: __label__pos text...
# Assume train.txt is prepared
model = fasttext.train_supervised(
    input="train.txt",
    epoch=10,
    lr=0.5,
    wordNgrams=2,
    dim=100,
)
model.save_model("quality-clf.bin")

# 2) Inference
clf = fasttext.load_model("quality-clf.bin")

def quality_score(text: str) -> float:
    labels, probs = clf.predict(text.replace("\n", " "), k=2)
    # Probability of __label__pos
    return float(probs[labels.index("__label__pos")]) if "__label__pos" in labels else 0.0

threshold = 0.5
keep = quality_score(doc) >= threshold
