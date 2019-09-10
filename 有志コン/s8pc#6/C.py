H, W = map(int, input().split())
c = [input() for _ in range(H)]
R = W * H
dp = [[False for _ in range(W * (2 * H - 1))] for _ in range(H)]

def dpf(i, j):
  if i ==  0:
    up = False
  else:
    up = dp[i - 1][j]
  if j == 0:
    left = False
  else:
    left = dp[i][j - 1]
  if i == 0 and j == 0:
    dp[i][j] = True
  elif c[i][j % W] == "." and (up or left):
    dp[i][j] = True
  else:
    dp[i][j] = False

for i in range(H):
  for j in range(R):
    dpf(i, j)

if dp[H - 1][R - 1]:
  print("Yay!")
else:
  print(":(")