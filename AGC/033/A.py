H, W = map(int, input().split())
A = []

queue = []
for i in range(H):
  A.append(list(input()))
  for j in range(W):
    if A[i][j] == "#":
      queue.append([i, j])
queue.append([H, W])
cnt = 0

while len(queue) > 1:
  i, j = queue.pop(0)
  if i == H and j == W:
    queue.append([H, W])
    cnt += 1
    continue
  if i > 0 and A[i - 1][j] == ".":
    A[i - 1][j] = "#"
    queue.append([i - 1, j])
  if i < H - 1 and A[i + 1][j] == ".":
    A[i + 1][j] = "#"
    queue.append([i + 1, j])
  if j > 0 and A[i][j - 1] == ".":
    A[i][j - 1] = "#"
    queue.append([i, j - 1])
  if j < W - 1 and A[i][j + 1] == ".":
    A[i][j + 1] = "#"
    queue.append([i, j + 1])
print(cnt)