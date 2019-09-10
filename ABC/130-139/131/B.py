N, L = map(int, input().split())

all = N * L + (N - 1) * N // 2
eat = float("inf")
for i in range(N):
  if abs(L + i) < abs(eat):
    eat = L + i
print(all - eat)