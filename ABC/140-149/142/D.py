A, B = map(int, input().split())

def gcd(a, b):
  while b != 0:
    a, b = b, a % b
  return(a)

g = gcd(A, B)
div = []
for i in range(1, int(g ** 0.5) + 1):
  if g % i == 0:
    div.append(i)
    if g // i != i:
      div.append(g // i)

div.sort()
ans = []
while len(div) != 0:
  d = div.pop(0)
  if d == 1:
    ans.append(d)
    continue
  div_c = div.copy()
  for i in range(len(div_c)):
    if div_c[i] % d == 0:
      div.remove(div_c[i])
  ans.append(d)

print(len(ans))