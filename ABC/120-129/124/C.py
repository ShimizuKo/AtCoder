S = input()
l = []
for s in S:
  l.append(s)

cnt = 0
for i in range(len(l)):
  if i != 0 and l[i - 1] == l[i]:
    if l[i] == "0":
      l[i] = "1"
    else:
      l[i] = "0"
    cnt += 1
print(cnt)