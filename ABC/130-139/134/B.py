N, D = map(int, input().split())
ans = N // (1 + 2 * D)
if N % (1 + 2 * D) != 0:
  ans += 1
print(ans)