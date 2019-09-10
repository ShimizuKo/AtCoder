N = int(input())
mas = [[] for _ in range(N - 1)]

for i in range(N - 1):
  b = int(input())
  mas[b - 1].append(i + 1)

bill = [1 for _ in range(N)]
for I in range(N - 1):
  i = N - I - 2
  if len(mas[i]) == 0:
    continue
  b_max = 0
  b_min = float("inf")
  for m in mas[i]:
    b_max = max(b_max, bill[m])
    b_min = min(b_min, bill[m])
  bill[i] = b_max + b_min + 1

print(bill[0])