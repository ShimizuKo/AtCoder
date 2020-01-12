N, M = map(int, input().split())
ac = [False for _ in range(N)]
wa = [0 for _ in range(N)]

ans_wa = 0
for _ in range(M):
  p, S = input().split()
  p = int(p) - 1
  if S == "AC":
    if ac[p] == False:
      ac[p] = True
      ans_wa += wa[p]
  else:
    wa[p] += 1

ans_ac = ac.count(True)
print("{} {}".format(ans_ac, ans_wa))