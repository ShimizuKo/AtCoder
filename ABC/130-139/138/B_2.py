N = int(input())
A = list(map(int, input().split()))

mul = 1
for a in A:
  mul *= a

den = 0
for a in A:
  den += mul / a

ans = mul / den
print(ans) 