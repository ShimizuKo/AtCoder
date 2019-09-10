import bisect
from collections import deque

N = int(input())
A = []
for _ in range(N):
  a = int(input())
  A.append(a)

b = deque([])
for a in A:
  if len(b) == 0:
    b.append(a)
  else:
    if a <= b[0]:
      b.appendleft(a)
    else:
      b[bisect.bisect_left(b, a) - 1] = a
print(len(b))