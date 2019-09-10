N = int(input())
A = []
for _ in range(N):
  a = int(input())
  A.append(a)

A_max = max(A)
max_index = A.index(A_max)
A.pop(max_index)
A_second = max(A)
for i in range(N):
  if i == max_index:
    print(A_second)
  else:
    print(A_max)