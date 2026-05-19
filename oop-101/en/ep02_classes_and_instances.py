class Book:
    def __init__(self, title: str, author: str) -> None:
        self.title = title
        self.author = author

    def summary(self) -> str:
        return f"{self.title} - {self.author}"


def build_sample_books() -> list[Book]:
    return [
        Book("Fluent Python", "Luciano Ramalho"),
        Book("Clean Code", "Robert C. Martin"),
    ]


if __name__ == "__main__":
    for book in build_sample_books():
        print(book.summary())
