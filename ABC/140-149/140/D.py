N, K = map(int, input().split())
S = list(input())

l = []
tmp = 0
for i in range(1, N):
  if S[i - 1] != S[i]:
    l.append([tmp, i - 1, i - tmp])
    tmp = i
  if i == N - 1:
    l.append([tmp, i, i - tmp + 1])

for k in range(K):
  i = 2 * k + 1
  if i >= len(l):
    break
  if S[l[i][0]] == "L":
    S[l[i][0] : l[i][1] + 1] = "R" * l[i][2]
  else:
    S[l[i][0] : l[i][1] + 1] = "L" * l[i][2]

ans = 0
for i in range(N - 1):
  if S[i] == S[i + 1]:
    ans += 1

print(ans)