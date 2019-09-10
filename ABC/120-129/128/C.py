N, M = map(int, input().split())

switch = []
for i in range(M):
  ks = input().split()
  k = int(ks[0])
  for j in range(k):
    if j == 0:
      switch.append([int(ks[j + 1]) - 1])
    else:
      switch[-1].append(int(ks[j + 1]) - 1)

p = list(map(int, input().split()))

com = 2 ** N
ans = 0
for i in range(com):
  cnt = 0
  for j in range(M):
    sw_cnt = 0
    for s in switch[j]:
      sw_cnt += int((i % (2 ** (s + 1))) / (2 ** s))
    if sw_cnt % 2 == p[j]:
      cnt += 1
  if cnt == M:
    ans += 1

print(ans)