import heapq

def minus_int(s):
  return -1 * int(s)

N, M = map(int, input().split())
A = list(map(minus_int, input().split()))
heapq.heapify(A)
for _ in range(M):
  tmp = int(heapq.heappop(A) / 2)
  heapq.heappush(A, tmp)

print(sum(A) * (-1))