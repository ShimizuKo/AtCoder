N, K = map(int, input().split())
x = list(map(int, input().split()))

length = float("inf")
for i in range(N - K + 1):
  r = i + K - 1
  l = i
  li = min(abs(x[r]) + abs(x[r] - x[l]), abs(x[l]) + abs(x[r] - x[l]))
  if li < length:
    length = li

print(length)