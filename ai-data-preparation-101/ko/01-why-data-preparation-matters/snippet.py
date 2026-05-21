"""Generated from book-content article."""

from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import re

categories = ["sci.space", "rec.autos"]
train = fetch_20newsgroups(subset="train", categories=categories)
test = fetch_20newsgroups(subset="test", categories=categories)

def clean(text: str) -> str:
    # headers, quotes, emails 제거
    text = re.sub(r"^(From|Subject|Lines|Organization):.*$", "", text, flags=re.M)
    text = re.sub(r"^>.*$", "", text, flags=re.M)
    text = re.sub(r"\S+@\S+", "", text)
    return text

def train_eval(train_texts, test_texts):
    vec = TfidfVectorizer(max_features=5000, stop_words="english")
    X_train = vec.fit_transform(train_texts)
    X_test = vec.transform(test_texts)
    clf = LogisticRegression(max_iter=1000).fit(X_train, train.target)
    pred = clf.predict(X_test)
    return accuracy_score(test.target, pred)

raw_acc = train_eval(train.data, test.data)
clean_acc = train_eval([clean(t) for t in train.data],
                        [clean(t) for t in test.data])
print(f"Raw:     {raw_acc:.4f}")
print(f"Cleaned: {clean_acc:.4f}")
