import math

a, b, x = map(int, input().split())
x_max = a * a * b

ans = 0
if x * 2 <= x_max:
  c = ((x * 2) / b) / a
  ans = math.acos(b / ((c ** 2 + b ** 2) ** 0.5))
else:
  c = ((x_max - x) * 2) / a / a
  ans = math.acos(c / ((c ** 2 + a ** 2) ** 0.5))
print(90 - math.degrees(ans))