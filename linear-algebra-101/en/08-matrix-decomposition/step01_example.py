import numpy as np


def run():
    np.random.seed(0)
    a = np.array([[3.0, 1.0], [1.0, 3.0], [1.0, 1.0]])
    u, s, vt = np.linalg.svd(a, full_matrices=False)
    recon = u @ np.diag(s) @ vt
    rank1 = np.outer(u[:, 0] * s[0], vt[0, :])
    print("singular values:", s)
    print("recon error:", np.linalg.norm(a - recon))
    return {"a": a, "u": u, "s": s, "vt": vt, "recon": recon, "rank1": rank1}


if __name__ == "__main__":
    run()
