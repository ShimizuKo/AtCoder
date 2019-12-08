N = int(input())
l = []
A = []
for i in range(N):
  A.append(int(input()))
  l.append([])
  for j in range(A[-1]):
    x, y = map(int, input().split())
    x -= 1
    l[-1].append([x, y])

mem = []
for i in range(2 ** N):
  mem.append(("{:0=15}".format(int(bin(i)[2:])))[15-N:])

ans = 0
for m in mem:
  f = True
  for i in range(N):
    if m[i] == "1":
      for li in l[i]:
        if str(li[1]) != m[li[0]]:
          f = False
          break
  if f:
    ans = max(ans, m.count("1"))
print(ans)