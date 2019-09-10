N = int(input())
L = [list(map(int, input().split())) for i in range(N)]

flag = False
ans = [0, 0, 0]
for i in range(101):
  for j in range(101):
    for k in range(N):
      Xt, Yt, Ht = L[k][0], L[k][1], L[k][2]
      if Ht > 0:
        break
    H = Ht + abs(Xt - i) + abs(Yt - j)
    result = []
    for l in L:
      if l[2] == max(H - abs(i - l[0]) - abs(j - l[1]), 0):
        result.append(True)
      else:
        result.append(False)
    if result.count(True) == N:
      ans[0], ans[1], ans[2] = i, j, H
      flag = True
      break
  if flag:
    break

print("{} {} {}".format(ans[0], ans[1], ans[2]))