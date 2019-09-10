N, K = map(int, input().split())
A = list(map(int, input().split()))
MOD = 10 ** 9 + 7

a = 0
b = 0
for i in range(N - 1):
  for j in range(i + 1, N):
    if A[i] > A[j]:
      a += 1
    if A[i] < A[j]:
      b += 1
ans = a * K * (K + 1) // 2
ans += b * K * (K - 1) // 2
print(ans % MOD)