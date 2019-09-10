S = input()
MOD = 10 ** 9 + 7
N = 13
dp = [0 for _ in range(N)]
dp[0] = 1

mul = 1
for i in range(len(S)):
  c = S[len(S) - i - 1]
  nextDP = [0 for _ in range(N)]

  if c == "?":
    for k in range(10):
      for j in range(N):
        nextDP[(k * mul + j) % N] += dp[j]
        nextDP[(k * mul + j) % N] %= MOD
  else:
    k = int(c)
    for j in range(N):
      nextDP[(k * mul + j) % N] += dp[j]
      nextDP[(k * mul + j) % N] %= MOD

  mul *= 10
  mul %= N
  dp = nextDP
print(dp[5])