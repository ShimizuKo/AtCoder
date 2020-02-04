N, K = map(int, input().split())
h = list(map(int, input().split()))

ans = 0
for hi in h:
  if hi >= K:
    ans += 1

print(ans)