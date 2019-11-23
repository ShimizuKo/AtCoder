N = int(input())
A = list(map(int, input().split()))

A_sum = 0
for Ai in A:
  A_sum += Ai

s1 = 0
i = 0
while s1 < A_sum / 2:
  s1 += A[i]
  i += 1

s2 = s1 - A[i - 1]
ans = min(abs(A_sum - s1 * 2), abs(A_sum - s2 * 2))
print(ans)