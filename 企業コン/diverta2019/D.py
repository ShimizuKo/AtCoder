N = int(input())

def make_divisors(n):
  divisors = []
  for i in range(1, int(n ** 0.5) + 1):
    if n % i == 0:
      divisors.append(i)
      if i != n // i:
        divisors.append(n // i)
  return divisors

div = make_divisors(N)
ans = 0
for d in div:
  if d != 1 and N // (d - 1) == N % (d - 1):
    ans += d - 1

print(ans)