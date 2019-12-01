N = int(input())
S = input()

pins = []
for i in range(10):
  for j in range(10):
    for k in range(10):
      pins.append(str(i) + str(j) + str(k))

ans = 0
for p in pins:
  i = S.find(p[0])
  if i >= 0:
    j = S[i + 1 :].find(p[1])
    if j >= 0:
      k = S[i + j + 2 :].find(p[2])
      if k >= 0:
        ans += 1
print(ans)