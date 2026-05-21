"""Generated from book-content article."""

theta = np.deg2rad(30)
R = np.array([[np.cos(theta), -np.sin(theta)],
              [np.sin(theta),  np.cos(theta)]])
pts = np.array([[1.0, 0.0], [0.0, 1.0], [1.0, 1.0]])
rot = pts @ R.T
print(rot)
