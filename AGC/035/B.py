N, M = map(int, input().split())
to = [[] for _ in range(N)]

for _ in range(M):
  A, B = map(int, input().split())
  A -= 1
  B -= 1
  to[A].append(B)
  to[B].append(A)

if M % 2 == 1:
  print(-1)
else:
  for i in range(N):
    if len(to[i]) < 2:
      continue
    else:
      for j in range(len(to[i]) // 2):
        d0, d1 = to[i][0], to[i][1]
        print("{} {}".format(i + 1, d0 + 1))
        print("{} {}".format(i + 1, d1 + 1))
        to[i].remove(d0)
        to[i].remove(d1)
        to[d0].remove(i)
        to[d1].remove(i)