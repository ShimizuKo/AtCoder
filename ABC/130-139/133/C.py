L, R = map(int, input().split())

flag = False
ans = float("inf")
for i in range(L, min(R + 1, L + 2018)):
  for j in range(i + 1, min(R + 1, L + 2019)):
    ans = min(ans, (i * j) % 2019)
    if ans == 0:
      flag = True
      break
  if flag:
    break
print(ans)