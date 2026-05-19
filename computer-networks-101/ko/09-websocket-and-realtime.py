from __future__ import annotations

import struct


def encode_masked_text_frame(payload: str, mask_key: bytes = b"ABCD") -> bytes:
    raw = payload.encode()
    first = 0x81
    second = 0x80 | len(raw)
    masked = bytes(byte ^ mask_key[i % 4] for i, byte in enumerate(raw))
    return bytes([first, second]) + mask_key + masked


def parse_websocket_frame(frame: bytes) -> dict[str, object]:
    first, second = frame[0], frame[1]
    fin = bool(first & 0x80)
    opcode = first & 0x0F
    masked = bool(second & 0x80)
    length = second & 0x7F
    idx = 2
    if length == 126:
        length = struct.unpack("!H", frame[idx:idx + 2])[0]
        idx += 2
    if length == 127:
        raise ValueError("large frames are not supported in this demo")
    mask_key = b""
    if masked:
        mask_key = frame[idx:idx + 4]
        idx += 4
    payload = frame[idx:idx + length]
    if masked:
        payload = bytes(byte ^ mask_key[i % 4] for i, byte in enumerate(payload))
    return {"fin": fin, "opcode": opcode, "payload": payload.decode()}


if __name__ == "__main__":
    sample = encode_masked_text_frame("hello")
    print(parse_websocket_frame(sample))
