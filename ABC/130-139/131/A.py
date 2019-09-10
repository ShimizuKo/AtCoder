S = input()
ans = "Good"

for i in range(3):
  if S[i + 1] == S[i]:
    ans = "Bad"
print(ans)