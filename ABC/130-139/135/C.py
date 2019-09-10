N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = 0
for i in range(N):
  if A[i] >= B[i]:
    ans += B[i]
  else:
    ans += A[i]
    tmp = B[i] - A[i]
    ans += min(A[i + 1], tmp)
    A[i + 1] = max(A[i + 1] - tmp, 0)

print(ans)