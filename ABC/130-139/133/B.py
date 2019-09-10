import numpy as np

N, D = map(int, input().split())
X = []
for _ in range(N):
  X.append(list(map(int, input().split())))

cnt = 0
for i in range(N):
  for j in range(i, N):
    if i == j:
      continue
    dis = 0
    for k in range(D):
      dis += (X[i][k] - X[j][k]) ** 2
    dist = np.sqrt(dis)
    if dist == int(dist):
      cnt += 1
print(cnt)