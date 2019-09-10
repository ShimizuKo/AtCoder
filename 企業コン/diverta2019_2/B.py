N = int(input())
xy = [list(map(int, input().split())) for _ in range(N)]

ans = float("inf")

if N < 3:
  ans = 1
else:   
  for i in range(N):
    x, y = xy[i][0], xy[i][1]
    for j in range(N):
      if i == j:
        continue
      p, q = xy[j][0] - x, xy[j][1] - y
      cnt = 0
      for k in range(N):
        xk, yk = xy[k][0], xy[k][1]
        for l in range(N):
          if k == l:
            continue
          if xy[l][0] - xk == p and xy[l][1] - yk == q:
            cnt += 1
      ans = min(ans, N - cnt)
print(ans)