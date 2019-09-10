N = int(input())

S = {}
for i in range(N):
  s = [0 for _ in range(26)]
  tmp = input()
  for j in range(10):
    s[ord(tmp[j]) - ord("a")] += 1
  
  s = ",".join(map(str, s))
  if s in S:
    S[s] += 1
  else:
    S[s] = 1

ans = 0
for v in S.values():
  if v > 1:
    for i in range(1, v):
      ans += i

print(ans)