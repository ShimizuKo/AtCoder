N, A, B, C = map(int, input().split())
MOD = 10 ** 9 + 7
A /= 100
B /= 100
C /= 100

com = [[1] * N for _ in range(N)]
def comb(m, n):
  if n == 0:
    return 1
  if m == n:
    return 1
  return com[m - 1][n - 1] + com[m - 1][n]

powA = [1]
powB = [1]
for i in range(N):
  powA.append((powA[-1] * A))
  powB.append((powB[-1] * B))

for i in range(2 * N):
  tmp = N + i - 1
  com.append(comb(tmp, N - 1))
Q = 1 - C
P = 0
for i in range(N, 2 * N):
  P += i * (powA[N] * powB[i - N] + powA[i - N] * powB[N]) * i * com[i - N]
print(P / Q)