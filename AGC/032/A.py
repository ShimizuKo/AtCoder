N = int(input())
b = list(map(int, input().split()))

b.reverse()
ans = []
disable = False

for i in range(N):
  for j in range(len(b)):
    if b[j] == len(b) - j:
      ans.append(b.pop(j))
      break
    if j == len(b) - 1:
      disable = True
      ans = [-1]
      break
  if disable:
    break

ans.reverse()
for a in ans:
  print(a)