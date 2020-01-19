N = int(input())

c = [[0 for _ in range(9)] for _ in range(9)]

for n in range(1, N + 1):
  l = n % 10
  if l == 0:
    continue
  t = n // (10 ** (len(str(n)) - 1))
  c[t - 1][l - 1] += 1

ans = 0
for i in range(9):
  for j in range(9):
    ans += c[i][j] * c[j][i]
print(ans)