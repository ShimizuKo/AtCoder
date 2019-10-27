N = int(input())

ans = 0
sq = int(N ** 0.5) + 1
for i in range(sq):
  n = sq - i
  if N % n == 0:
    ans = n + N // n - 2
    break
print(ans)