N, T = map(int, input().split())
ct = []
for i in range(N):
  c, t = map(int, input().split())
  ct.append([c, t])

def kitaku(l):
  l.sort()
  for i in range(N):
    if l[i][1] <= T:
      return l[i][0]
    if i == N - 1:
      return "TLE"

print(kitaku(ct))