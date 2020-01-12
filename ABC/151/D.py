H, W = map(int, input().split())
S = []
di = [-1, 0, 1, 0]
dj = [0, -1, 0, 1]
for _ in range(H):
  S.append(input())

ans = 0
for si in range(H):
  for sj in range(W):
    if S[si][sj] == "#":
      continue
    dist = [[-1 for _ in range(W)] for _ in range(H)]
    dist[si][sj] = 0
    queue = [[si, sj]]
    while len(queue) > 0:
      q = queue.pop(0)
      i = q[0]
      j = q[1]
      for dir in range(4):
        ni = i + di[dir]
        nj = j + dj[dir]
        if ni < 0 or ni >= H or nj < 0 or nj >= W:
          continue
        if S[ni][nj] == "#":
          continue
        if dist[ni][nj] == -1:
          dist[ni][nj] = dist[i][j] + 1
          queue.append([ni, nj])
    for i in range(H):
      for j in range(W):
        ans = max(ans, dist[i][j])

print(ans)