# pip install tokenizers
from tokenizers import Tokenizer
from tokenizers.models import BPE
from tokenizers.trainers import BpeTrainer
from tokenizers.pre_tokenizers import ByteLevel

tokenizer = Tokenizer(BPE(unk_token="<unk>"))
tokenizer.pre_tokenizer = ByteLevel()

trainer = BpeTrainer(
    vocab_size=32000,
    special_tokens=["<pad>", "<unk>", "<s>", "</s>", "<mask>"],
    min_frequency=2,
)

files = ["data/corpus_ko.txt", "data/corpus_en.txt"]
tokenizer.train(files, trainer)
tokenizer.save("custom-bpe-32k.json")

# it 사용
loaded = Tokenizer.from_file("custom-bpe-32k.json")
ids = loaded.encode("Hello 안녕하세요").ids
print(ids, "->", loaded.decode(ids))
