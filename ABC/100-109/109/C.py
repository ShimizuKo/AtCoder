N, X = map(int, input().split())
x = list(map(int, input().split()))
x_diff = [abs(x[i] - X) for i in range(N)]

def gcd(m, n):
  a = max(m, n)
  b = min(m, n)
  if a % b == 0:
    return b
  else:
    return gcd(b, a % b)

D = x_diff[0]
for i in range(1, N):
  D = gcd(D, x_diff[i])
print(D)