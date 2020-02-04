N = int(input())
A = list(map(int, input().split()))

l = []
for i in range(1, N + 1):
  l.append([A[i - 1], i])
l.sort()

for i in range(N):
  print(l[i][1], end = "")
  if i == N - 1:
    print()
  else:
    print(" ", end = "")