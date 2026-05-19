from common import MockImageEncoder, MockTextEncoder, cosine_sim, synthetic_image


def run(text: str = "checkerboard") -> float:
    image_vec = MockImageEncoder().encode(synthetic_image(8))
    text_vec = MockTextEncoder().encode(text)
    return cosine_sim(image_vec, text_vec)
