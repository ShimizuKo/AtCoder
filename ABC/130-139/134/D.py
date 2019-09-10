N = int(input())
a = list(map(int, input().split()))

def make_divisors(n):
  divisors = []
  for i in range(1, int(n ** 0.5) + 1):
    if n % i == 0:
      divisors.append(i)
      if i != n // i:
        divisors.append(n // i)
  return divisors

a.reverse()
check = [0 for _ in range(N + 1)]
ball = []
for i in range(N):
  if check[N - i] % 2 != a[i]:
    ball.append(N - i)
    div = make_divisors(N - i)
    for d in div:
      check[d] += 1

print(len(ball))
for i in range(len(ball)):
  print(ball[i], end = "")
  if i != len(ball) - 1:
    print(" ", end = "")
  else:
    print()