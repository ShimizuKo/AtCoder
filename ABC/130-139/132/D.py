N, K = map(int, input().split())
MOD = 1000000007

fact = [1]
for i in range(1, N * 2):
  fact.append(fact[-1] * i)

def comb(n, k):
  return (fact[n] // (fact[n - k] * fact[k])) % MOD

def f2(n, k):
  return comb(n + k - 1, k - 1)

def f(n, k):
  if n < k:
    return 0
  if n == 0 and k == 0:
    return 1
  if k < 1:
    return 0
  return f2(n - k, k)

for i in range(1, K + 1):
  blue = f(K, i)
  red = (f(N - K, i - 1) + 2 * f(N - K, i) + f(N - K, i + 1)) % MOD
  ans = blue * red
  print(ans % MOD)