N, T = map(int, input().split())
A = list(map(int, input().split()))

sums = 0
for a in A:
  sums += a

ans = int(sums / T)
if sums % T != 0:
  ans += 1

print(ans)