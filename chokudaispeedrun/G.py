N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]

def gcd(a, b):
  if a < b:
    a, b = b, a
  if b == 0:
    return a
  c = a % b
  return gcd(b, c)

for ab in AB:
  print(gcd(ab[0], ab[1]))