N, Q = map(int, input().split())
s = input()
td = [list(input().split()) for _ in range(Q)]

def goL(n):
  reach = False
  for tdi in td:
    if tdi[0] == s[n]:
      if tdi[1] == "L":
        n -= 1
        if n == -1:
          reach = True
          break
      if tdi[1] == "R":
        n += 1
        if n == N:
          break
  return reach

def goR(n):
  reach = False
  for tdi in td:
    if tdi[0] == s[n]:
      if tdi[1] == "L":
        n -= 1
        if n == -1:
          break
      if tdi[1] == "R":
        n += 1
        if n == N:
          reach = True
          break
  return reach

l = int(N / 2)
wid = l
ans_l = 0
while True:
  wid = int(wid / 2)
  result = goL(l)
  if result:
    l += wid
    ans_l = l
  else:
    l -= wid
  if wid == 0:
    break

r = int(N / 2)
wid = r
ans_r = N - 1
while True:
  wid = int(wid / 2)
  result = goR(r)
  if result:
    r -= wid
    ans_r = r
  else:
    r += wid
  if wid == 0:
    break

print(ans_r - ans_l)