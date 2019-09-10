A, B = map(int, input().split())

def xor(n):
  if n % 2 == 0:
    if int(n / 2) % 2 == 0:
      return n
    else:
      return n ^ 1
  else:
    if int((n + 1) / 2) % 2 == 0:
      return 0
    else:
      return 1

if A == B:
  print(A)
else:
  print(xor(A - 1) ^ xor(B))