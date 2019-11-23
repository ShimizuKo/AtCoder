X, Y = map(int, input().split())

def money(n):
  ret = 0
  if n == 1:
    ret = 300000
  elif n == 2:
    ret = 200000
  elif n == 3:
    ret = 100000
  
  return ret 

ans = 0
ans += money(X) + money(Y)
if X == 1 and Y == 1:
  ans += 400000
print(ans)