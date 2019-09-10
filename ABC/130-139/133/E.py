MOD = 1000000007

N, K = map(int, input().split())

fact = [1]
for i in range(1, K + 1):
  fact.append((fact[-1] * i) % MOD)

def pow_MOD(x, n):
  if n == 0:
    return 1
  if n % 2 == 0:
    return pow_MOD(x * x % MOD, n // 2)
  else:
    return x * pow_MOD(x * x % MOD, (n - 1) // 2) % MOD

def P(n, k):
  if n < k:
    return 0
  if k == 0:
    return 1
  return fact[n] * pow_MOD(fact[n - k], MOD - 2)

g = [[] for _ in range(N + 1)]
for i in range(N - 1):
  a, b = map(int, input().split())
  a -= 1
  b -= 1
  g[a].append(b)
  g[b].append(a)

s = 0
Q = [s]
ans = 1
searched = [False] * N
searched[s] = True
while len(Q) != 0:
  v = Q.pop(0)
  nk = K - 2
  c = len(g[v]) - 1
  if v == s:
    nk = K
    c = len(g[v]) + 1
  ans *= P(nk, c)
  for i in g[v]:
    if searched[i]:
      continue
    searched[i] = True
    Q.append(i)
print(ans % MOD)