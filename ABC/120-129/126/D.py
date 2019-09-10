N = int(input())
to = [[] for _ in range(N)]
cost = [[] for _ in range(N)]

for _ in range(N - 1):
  a, b, w = map(int, input().split())
  a -= 1
  b -= 1
  to[a].append(b)
  to[b].append(a)
  cost[a].append(w)
  cost[b].append(w)

ans = [-1 for _ in range(N)]
queue = []
queue.append(0)
while len(queue) > 0:
  v = queue.pop(0)
  for i in range(len(to[v])):
    u = to[v][i]
    w = cost[v][i]
    if ans[u] != -1:
      continue
    ans[u] = (ans[v] + w) % 2
    queue.append(u)

for a in ans:
  print(a)