N, K = map(int, input().split())
V = list(map(int, input().split()))

R = min(N, K)
l = []
ans = 0
for a in range(R + 1):
  for b in range(R + 1 - a):
    l = V[:a] + V[N - b:]
    l.sort()
    for i in range(K - a - b + 1):
      ans = max(ans, sum(l[i:]))
print(max(ans, 0))