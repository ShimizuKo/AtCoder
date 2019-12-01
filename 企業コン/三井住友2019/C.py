X = int(input())
N = X // 100
n = X % 100

if N == 0:
  print(0)
elif n / N > 5:
  print(0)
else:
  print(1)