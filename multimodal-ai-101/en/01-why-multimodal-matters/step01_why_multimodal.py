from common import synthetic_image


def run() -> dict[str, object]:
    image = synthetic_image(1)
    return {"shape": image.shape, "message": "multimodal combines modalities"}
