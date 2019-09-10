N = int(input())
A = list(map(int, input().split()))

ans = 0
for i in range(N):
  tmp = ans
  if i == 0:
    for j in range(N):
      if j % 2 == 0:
        ans += A[j]
      else:
        ans -= A[j]
  else:
    ans = 2 * A[i - 1] - tmp

  tmp = ans
  print(ans, end = "")
  if i != N - 1:
    print(" ", end = "")
  else:
    print()