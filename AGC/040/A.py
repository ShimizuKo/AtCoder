S = input()
N = len(S) + 1

n = [0]
for i in range(1, N + 1):
  n.append(n[-1] + i)

ans = 0
cnt_L = 0
cnt_R = 0
for i in range(N - 1):
  if i == 0:
    if S[i] == "<":
      cnt_L += 1
    else:
      cnt_R += 1
  elif S[i] != S[i - 1] and S[i] == "<":
    if cnt_L > 0:
      ans += n[max(cnt_L, cnt_R)] + n[min(cnt_L, cnt_R) - 1]
    else:
      ans += n[cnt_R]

    cnt_L = 1
    cnt_R = 0
  else:
    if S[i] == "<":
      cnt_L += 1
    else:
      cnt_R += 1
if S[-1] == "<":
  ans += n[cnt_L]
else:
  if cnt_L > 0:
    ans += n[max(cnt_L, cnt_R)] + n[min(cnt_L, cnt_R) - 1]
  else:
    ans += n[cnt_R]
print(ans)