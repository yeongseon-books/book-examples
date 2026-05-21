# 차원별 평균 거리 변화 확인
for d in [2, 10, 50, 100]:
    samples = np.random.randn(100, d)
    # 모든 쌍 간 평균 거리
    distances = []
    for i in range(10):
        for j in range(i+1, 10):
            dist = np.linalg.norm(samples[i] - samples[j])
            distances.append(dist)
    print(f'{d}차원: 평균 거리 = {np.mean(distances):.2f}, std = {np.std(distances):.2f}')
