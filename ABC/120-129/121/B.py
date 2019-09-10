N, M, C = map(int, input().split())
B = list(map(int, input().split()))
A = [list(map(int, input().split())) for i in range(N)]

cnt = 0
for i in range(N):
  ans = C
  for j in range(M):
    ans += A[i][j] * B[j]
  if ans > 0:
    cnt += 1
print(cnt)