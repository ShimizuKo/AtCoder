H, W = map(int, input().split())
a = [input() for _ in range(H)]
h = [True for _ in range(H)]
w = [True for _ in range(W)]

for i in range(H):
  if a[i].count(".") == W:
    h[i] = False

for i in range(W):
  cnt = 0
  for j in range(H):
    if a[j][i] == ".":
      cnt += 1
  if cnt == H:
    w[i] = False

for i in range(H):
  for j in range(W):
    if h[i] and w[j]:
      print(a[i][j], end = "")
  if h[i]:
    print("")