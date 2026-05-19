from common import safe_eval_arith

def repl_once(expr: str) -> float:
    return safe_eval_arith(expr)

if __name__ == "__main__":
    print(repl_once("(1+2)*3"))
