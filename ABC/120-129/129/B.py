N = int(input())
W = list(map(int, input().split()))

S = [0]
for w in W:
  S.append(S[-1] + w)

ans = float("inf")
for i in range(N):
  ans = min(ans, abs(S[-1] - S[i] * 2))
print(ans)