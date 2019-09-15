S = input()

ans = "Yes"
for i in range(len(S)):
  if i % 2 == 0 and S[i] == "L" or i % 2 == 1 and S[i] == "R":
    ans = "No"
    break
print(ans)