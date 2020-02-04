N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

ans = 0
for i in range(N):
  a = A[i] - 1
  ans += B[a]
  if i != 0 and a == A[i - 1]:
    ans += C[A[i - 1] - 1]
print(ans)