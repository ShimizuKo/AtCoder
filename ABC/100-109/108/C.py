N, K = map(int, input().split())

ans = 0
if K % 2 == 1:
  ans = int(N / K) ** 3
else:
  cnt = 0
  for i in range(1, N + 1):
    if i % K == int(K / 2):
      cnt += 1
  ans = int(N / K) ** 3 + cnt ** 3

print(ans)