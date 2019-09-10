N = int(input())

V = 100005
to = [[] for _ in range(V * 2)]
visited = [False for _ in range(V * 2)]
cnt = []

def dfs(v):  
  L = [v]
  while len(L) > 0:
    l = L.pop(0)
    if visited[l]:
      continue
    visited[l] = True
    cnt[l // V] += 1
    for u in to[l]:
      L.append(u)

for i in range(N):
  x, y = map(int, input().split())
  y += V
  to[x].append(y)
  to[y].append(x)

ans = 0
for i in range(V * 2):
  if visited[i]:
    continue
  cnt = [0, 0]
  dfs(i)
  ans += cnt[0] * cnt[1]
ans -= N
print(ans)