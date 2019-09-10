N, K = map(int, input().split())

def percentage(n):
  if n >= K:
    return 1
  
  return percentage(n * 2) / 2

ans = 0
for i in range(1, N + 1):
  ans += percentage(i) / N

print(ans)