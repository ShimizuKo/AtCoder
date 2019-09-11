from collections import deque

N, Q = map(int, input().split())

to = [[] for _ in range(N)]
for _ in range(N - 1):
  a, b = map(int, input().split())
  a -= 1
  b -= 1
  to[a].append(b)
  to[b].append(a)

cnt = [0 for _ in range(N)]
for _ in range(Q):
  p, x = map(int, input().split())
  p -= 1
  cnt[p] += x

queue = deque()
queue.append((0, -1))
while queue:
  q = queue.popleft()
  if q[0] != 0:
    cnt[q[0]] += cnt[q[1]]
  for i in to[q[0]]:
    if i != q[1]:
      queue.append((i, q[0]))

for c in cnt:
  print(c)