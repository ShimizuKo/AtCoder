A, B, C = map(int, input().split())
sound = int(B / A)
if sound < C:
  print(sound)
else:
  print(C)