W, H, x, y = map(int, input().split())

ans = W * H / 2
multi = 0
if x == W / 2 and y == H / 2:
  multi = 1
print("{} {}".format(ans, multi))