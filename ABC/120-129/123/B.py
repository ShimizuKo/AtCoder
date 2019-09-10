menu = [int(input()) for _ in range(5)]

cnt = 0
l = [10]
for m in menu:
  cnt += m
  mod = cnt % 10
  if mod != 0:
    cnt += 10 - mod
    l.append(mod)

cnt -= 10 - min(l)
print(cnt)