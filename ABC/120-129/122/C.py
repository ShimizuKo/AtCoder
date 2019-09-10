N, Q = map(int, input().split())
S = input()

AC_list = []
cnt = 0
for i in range(N):
  if i != 0 and S[i - 1] == "A" and S[i] == "C":
    cnt += 1
  AC_list.append(cnt)

for _ in range(Q):
  l, r = map(int, input().split())
  print(AC_list[r - 1] - AC_list[l - 1])