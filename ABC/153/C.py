N, K = map(int, input().split())
H = list(map(int, input().split()))

ans = 0
if N > K:
  H.sort()
  ans = sum(H[:N - K])
print(ans)