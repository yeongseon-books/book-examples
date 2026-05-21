"""Generated from book-content article."""

from typing import List


class ChunkedProcessor:
    """Process long input by splitting into chunks"""

    def __init__(self, api_key: str, chunk_size: int = 3000):
        self.client = OpenAI(api_key=api_key)
        self.chunk_size = chunk_size
        self.encoding = tiktoken.encoding_for_model("gpt-4o")

    def split_into_chunks(self, text: str) -> list[str]:
        """Split text into chunks by token count"""
        tokens = self.encoding.encode(text)
        chunks = []

        for i in range(0, len(tokens), self.chunk_size):
            chunk_tokens = tokens[i:i + self.chunk_size]
            chunk_text = self.encoding.decode(chunk_tokens)
            chunks.append(chunk_text)

        return chunks

    def process_long_document(self, document: str, query: str) -> str:
        """Process long document chunk-by-chunk and combine results"""
        chunks = self.split_into_chunks(document)
        results = []

        for i, chunk in enumerate(chunks):
            response = self.client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": "Answer the query based on the given text chunk."},
                    {"role": "user", "content": f"Query: {query}\n\nChunk {i+1}/{len(chunks)}:\n{chunk}"}
                ],
                temperature=0
            )

            results.append(response.choices[0].message.content)

        # Combine final results
        final_response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "Combine the following answers into a coherent response."},
                {"role": "user", "content": "\n\n".join(results)}
            ],
            temperature=0
        )

        return final_response.choices[0].message.content

# Usage example
processor = ChunkedProcessor(api_key="your-api-key", chunk_size=3000)

long_document = "very long document content..." * 5000  # 100K+ tokens
query = "What's the key summary of this document?"

answer = processor.process_long_document(long_document, query)
print(answer)
