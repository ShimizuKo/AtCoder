N = int(input())
S = input()
K = int(input())

sk = S[K - 1]
ans = ""
for s in S:
  if s == sk:
    ans += s
  else:
    ans += "*"
print(ans)