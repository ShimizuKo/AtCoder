H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]

cnt = [[0 for _ in range(W)] for _ in range(H)]
for i in range(H):
  done = [0 for _ in range(W)]
  for j in range(W):
    if S[i][j] == "#":
      continue
    if done[j]:
      continue
    l = 0
    while j + l < W:
      if S[i][j + l] == "#":
        break
      l += 1
    for k in range(l):
      cnt[i][j + k] += l
      done[j + k] = 1

for j in range(W):
  done = [0 for _ in range(H)]
  for i in range(H):
    if S[i][j] == "#":
      continue
    if done[i]:
      continue
    l = 0
    while i + l < H:
      if S[i + l][j] == "#":
        break
      l += 1
    for k in range(l):
      cnt[i + k][j] += l
      done[i + k] = 1

ans = 0
for i in range(H):
  for j in range(W):
    ans = max(ans, cnt[i][j] - 1)
print(ans)