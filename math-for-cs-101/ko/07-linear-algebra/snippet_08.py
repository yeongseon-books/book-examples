"""Generated from book-content article."""

def rotation(theta_rad: float) -> np.ndarray:
    c, s = np.cos(theta_rad), np.sin(theta_rad)
    return np.array([[c, -s], [s, c]])

p = np.array([1.0, 0.0])
p_rot = rotation(np.pi / 2) @ p
