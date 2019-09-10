K, X = map(int, input().split())

ans = []
for i in range(X - K + 1, X + K):
  ans.append(i)

N = len(ans)
for i in range(N):
  print(ans[i], end = "")
  if i == N - 1:
    print()
  else:
    print(" ", end = "")