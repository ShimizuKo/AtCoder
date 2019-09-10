N, M = map(int, input().split())

to = [[] for _ in range(N)]
dist = [[0 for _ in range(3)] for _ in range(100005)]
for i in range(M):
  a, b = map(int, input().split())
  a -= 1
  b -= 1
  to[a].append(b)

sv, tv = map(int, input().split())
sv -= 1
tv -= 1

for i in range(N):
  for j in range(3):
    dist[i][j] = float("inf")
q = [[sv, 0]]
dist[sv][0] = 0
while len(q) != 0:
  v = q[0][0]
  l = q[0][1]
  q.pop(0)
  for u in to[v]:
    nl = (l + 1) % 3
    if dist[u][nl] != float("inf"):
      continue
    dist[u][nl] = dist[v][l] + 1
    q.append([u, nl])
ans = dist[tv][0]
if ans == float("inf"):
  ans = -1
else:
  ans //= 3
print(ans)