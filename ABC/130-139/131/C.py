A, B, C, D = map(int, input().split())

def gcd(a, b):
  while b != 0:
    a, b = b, a % b
  return a

def lcm(a, b):
  return a * b // gcd(a, b)

def f(x):
  return x - x // C - x // D + x // lcm(C, D) 

ans = f(B) - f(A - 1)
print(ans)