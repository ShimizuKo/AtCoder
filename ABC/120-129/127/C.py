N, M = map(int, input().split())

tmpL = 0
tmpR = float("inf")
for i in range(M):
  L, R = map(int, input().split())
  tmpL = max(tmpL, L)
  tmpR = min(tmpR, R)

if tmpR - tmpL < 0:
  print(0)
else:
  print(tmpR - tmpL + 1)