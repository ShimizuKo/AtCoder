N, K = map(int, input().split())
S = input()

ans = K * 2
for i in range(N - 1):
  if S[i] == S[i + 1]:
    ans += 1
ans = min(ans, N - 1)
print(ans)