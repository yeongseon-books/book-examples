# generate.py
import argparse, torch
from data import decode, encode
from model import GPT, GPTConfig

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--prompt", type=str, default="ROMEO:")
    parser.add_argument("--max", type=int, default=200)
    parser.add_argument("--temp", type=float, default=0.8)
    parser.add_argument("--top_k", type=int, default=20)
    parser.add_argument("--top_p", type=float, default=0.9)
    args = parser.parse_args()
    device = "cuda" if torch.cuda.is_available() else "cpu"
    ckpt = torch.load("ckpt.pt", map_location=device)
    config = GPTConfig(**ckpt["config"])
    model = GPT(config).to(device)
    model.load_state_dict(ckpt["model"]); model.eval()
    idx = torch.tensor([encode(args.prompt)], dtype=torch.long, device=device)
    with torch.no_grad(): out = model.generate(idx, args.max, args.temp, args.top_k, args.top_p)
    print(decode(out[0].tolist()))

if __name__ == "__main__":
    main()
