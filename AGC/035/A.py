N = int(input())
A = list(map(int, input().split()))

tmp = 0
for a in A:
  tmp ^= a

ans = "No"
if tmp == 0:
  ans = "Yes"
print(ans)