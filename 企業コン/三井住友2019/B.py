N = int(input())

ans = ":("
for x in range(1, N + 1):
  n = int(x * 1.08)
  if n == N:
    ans = x
    break
print(ans)