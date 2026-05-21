"""Generated from book-content article."""

import numpy as np
import matplotlib.pyplot as plt

def plot_transformation(T, title):
    """
    행렬 T를 단위 정사각형에 적용하고 결과를 그립니다.
    """
    # 단위 정사각형 꼭짓점
    square = np.array([[0, 1, 1, 0, 0],
                       [0, 0, 1, 1, 0]])
    
    # 변환 적용
    transformed = T @ square
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
    
    # 원본
    ax1.plot(square[0], square[1], 'b-o', linewidth=2, markersize=8)
    ax1.set_xlim(-2, 2)
    ax1.set_ylim(-2, 2)
    ax1.set_aspect('equal')
    ax1.grid(True, alpha=0.3)
    ax1.axhline(0, color='k', linewidth=0.5)
    ax1.axvline(0, color='k', linewidth=0.5)
    ax1.set_title('Original')
    
    # 변환 후
    ax2.plot(transformed[0], transformed[1], 'r-o', linewidth=2, markersize=8)
    ax2.plot(square[0], square[1], 'b--', alpha=0.3, linewidth=1)
    ax2.set_xlim(-2, 2)
    ax2.set_ylim(-2, 2)
    ax2.set_aspect('equal')
    ax2.grid(True, alpha=0.3)
    ax2.axhline(0, color='k', linewidth=0.5)
    ax2.axvline(0, color='k', linewidth=0.5)
    ax2.set_title(title)
    
    plt.tight_layout()
    return fig

# 1. 회전 (45도)
theta = np.pi / 4
R = np.array([[np.cos(theta), -np.sin(theta)],
              [np.sin(theta),  np.cos(theta)]])
fig1 = plot_transformation(R, 'Rotation 45°')
plt.savefig('rotation.png', dpi=100, bbox_inches='tight')
plt.close()

# 2. 축소/확대
S = np.array([[2.0, 0.0],
              [0.0, 0.5]])
fig2 = plot_transformation(S, 'Scaling (2x, 0.5y)')
plt.savefig('scaling.png', dpi=100, bbox_inches='tight')
plt.close()

# 3. 반사 (x축)
F = np.array([[1.0, 0.0],
              [0.0, -1.0]])
fig3 = plot_transformation(F, 'Reflection (x-axis)')
plt.savefig('reflection.png', dpi=100, bbox_inches='tight')
plt.close()

# 4. 전단
Sh = np.array([[1.0, 0.5],
               [0.0, 1.0]])
fig4 = plot_transformation(Sh, 'Shear (x-direction)')
plt.savefig('shear.png', dpi=100, bbox_inches='tight')
plt.close()

# 5. 합성 변환
M = Sh @ R @ S
fig5 = plot_transformation(M, 'Composite: Shear ∘ Rotation ∘ Scale')
plt.savefig('composite.png', dpi=100, bbox_inches='tight')
plt.close()

print('변환 결과가 이미지로 저장되었습니다.')
