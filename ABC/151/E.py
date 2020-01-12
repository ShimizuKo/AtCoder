N, K = map(int, input().split())
A = list(map(int, input().split()))
MOD = 10 ** 9 + 7

kai1 = [1, 1]
kai2 = [1, 1]
inverse = [0, 1]
for i in range(2, N + 1):
  kai1.append((kai1[-1] * i) % MOD)
  inverse.append((-inverse[MOD % i] * (MOD // i)) % MOD)
  kai2.append((kai2[-1] * inverse[-1]) % MOD)


def comb(n, r):
  if r < 0 or r > n:
    return 0
  r = min(r, n - r)
  return (kai1[n] * kai2[r] * kai2[n - r]) % MOD

if K >= 2:
  A.sort(reverse = True)
  maxS = 0
  minS = 0
  for i in range(N - K + 1):
    maxS += A[i] * comb(N - i - 1, K - 1)
    maxS %= MOD
  A.sort()
  for i in range(N - K + 1):
    minS += A[i] * comb(N - i - 1, K - 1)
    minS %= MOD
  print((maxS - minS) % MOD)
else:
  print(0)