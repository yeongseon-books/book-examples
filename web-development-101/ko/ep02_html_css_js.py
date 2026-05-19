"""Web Development 101 - Episode 2: Html css js."""

from html.parser import HTMLParser


class _StructureParser(HTMLParser):
    """Parse HTML to extract structural metadata."""

    def __init__(self):
        super().__init__()
        self.h1_count = 0
        self.has_charset = False
        self.has_viewport = False

    def handle_starttag(self, tag, attrs):
        """Track h1 tags and meta attributes."""
        if tag == "h1":
            self.h1_count += 1
        if tag == "meta":
            attr_dict = dict(attrs)
            if attr_dict.get("charset"):
                self.has_charset = True
            if attr_dict.get("name") == "viewport":
                self.has_viewport = True


def run(filepath: str) -> dict:
    """Validate HTML structure from a file path."""
    with open(filepath, encoding="utf-8") as f:
        html = f.read()
    parser = _StructureParser()
    parser.feed(html)
    return {
        "h1_count": parser.h1_count,
        "has_charset": parser.has_charset,
        "has_viewport": parser.has_viewport,
    }
