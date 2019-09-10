N = int(input())
b = list(map(int, input().split()))
ans = []

for i in range(N):
  if b[i] > i:
    ans = [-1]
    break
  ans.insert(b[i] - 1, b[i])

for a in ans:
  print(ans)