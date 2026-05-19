import numpy as np
from common import pca_fit, text_histogram


def run():
    np.random.seed(0)
    rng = np.random.default_rng(0)
    x = rng.normal(size=(120, 2))
    x[:, 1] = 0.85 * x[:, 0] + 0.2 * rng.normal(size=120)
    comps, z, ratio, xc = pca_fit(x, n_components=1)
    hist = text_histogram(z[:, 0], bins=8, width=16)
    print('explained variance ratio pc1:', ratio[0])
    for line in hist:
        print(line)
    return {'x': x, 'xc': xc, 'components': comps, 'z': z, 'ratio': ratio, 'hist': hist}


if __name__ == '__main__':
    run()
