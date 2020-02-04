H = int(input())

ans = 0
atack = 1
while H > 0:
  ans += atack
  H //= 2
  atack *= 2
print(ans)