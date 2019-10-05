S = input()
K = int(input())

ans = 0
if len(S) == 1:
  ans = K // 2
else:
  S_2 = S + S
  once = 0
  cnt = 1
  for i in range(1, len(S)):
    if S[i - 1] == S[i]:
      cnt += 1
    else:
      once += cnt // 2
      cnt = 1
  once += cnt // 2
  if cnt == len(S):
    ans = len(S) * K // 2
  else:
    other = -once
    cnt = 1
    for i in range(1, len(S_2)):
      if S_2[i - 1] == S_2[i]:
        cnt += 1
      else:
        other += cnt // 2
        cnt = 1
    other += cnt // 2
    ans = once + other * (K - 1)
print(ans)