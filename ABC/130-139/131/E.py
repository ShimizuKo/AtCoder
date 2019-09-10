N, K = map(int, input().split())

if K > (N - 1) * (N - 2) // 2:
  print(-1)
else:
  M = N - 1 + (N - 1) * (N - 2) // 2 - K
  print(M)
  for i in range(N - 1):
    print("1 {}".format(i + 2))
  M -= N - 1
  a = N
  b = N - 1
  while M > 0:
    print("{} {}".format(a, b))
    b -= 1
    if b == 1:
      a -= 1
      b = a - 1
    M -= 1