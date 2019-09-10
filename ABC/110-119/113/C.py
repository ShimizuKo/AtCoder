N, M = map(int, input().split())
iPYx = []
for i in range(M):
  P, Y = map(int, input().split())
  iPYx.append([i, P, Y])

iPYx.sort(key = lambda x: (x[1], x[2]))
cnt = 0
for i in range(M):
  if i == 0 or iPYx[i][1] != iPYx[i - 1][1]:
    cnt = 1
  else:
    cnt += 1
  iPYx[i].append(cnt)
iPYx.sort(key = lambda x: x[0])
for i in range(M):
  print("{:06}{:06}".format(iPYx[i][1], iPYx[i][3]))