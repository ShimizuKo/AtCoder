N, K = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
s = 0
j = 0
for i in range(N):
  while j < N and s + A[j] < K:
    s += A[j]
    j += 1
  ans += j - i
  s -= A[i]
print(N * (N + 1) // 2 - ans)