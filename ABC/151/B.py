N, K, M = map(int, input().split())
A = list(map(int, input().split()))

score = 0
for a in A:
  score += a

ans = N * M - score
if ans > K:
  print(-1)
else:
  print(max(0, ans))