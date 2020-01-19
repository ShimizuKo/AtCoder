N = int(input())

c = [[0 for _ in range(9)] for _ in range(9)]
for i in range(1, 10):
  for j in range(1, 10):
    cnt = 0
    for n in range(1, N + 1):
      if n // (10 ** (len(str(n)) - 1)) == i and n % 10 == j:
        cnt += 1
    c[i - 1][j - 1] = cnt

ans = 0
for i in range(9):
  for j in range(9):
    ans += c[i][j] * c[j][i]
print(ans)