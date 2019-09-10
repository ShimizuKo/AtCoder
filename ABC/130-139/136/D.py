S = input()
N = len(S)

ans = []
RL = []
s = "R"
for i in range(1, N):
  if S[i] == "L" or S[i] == "R" and S[i - 1] == "R":
    s += S[i]
  else:
    RL.append(s)
    s = "R"
RL.append(s)

for rl in RL:
  for i in range(len(rl)):
    if rl[i] == "R" and rl[i + 1] == "L" or rl[i] == "L" and rl[i - 1] == "R":
      if i % 2 == 1:
        ans.append(len(rl) // 2)
      else:
        ans.append((len(rl) + 1) // 2)
    else:
      ans.append(0)

for i in range(N):
  print(ans[i], end = "")
  if i == N - 1:
    print()
  else:
    print(" ", end = "")