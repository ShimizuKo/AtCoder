A, B = map(int, input().split())

if A <= 5:
  print(0)
elif A <= 12:
  print(int(B / 2))
else:
  print(B)