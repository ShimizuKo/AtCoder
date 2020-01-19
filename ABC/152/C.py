N = int(input())
P = list(map(int, input().split()))

ans = 0
n = float("inf")
for p in P:
  if p <= n:
    ans += 1
    n = p
print(ans)