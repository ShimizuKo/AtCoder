from heapq import heappush, heappop

N, M = map(int, input().split())
jobs = [[] for _ in range(M)]

for i in range(N):
  ab = list(map(int, input().split()))
  #Ai > M の仕事はいらない
  if ab[0] <= M:
    jobs[ab[0] - 1].append(ab[1])

#最終日はAi=1の仕事のみ選べる。その前の日はAi<=2, ...
#終わりから考えればよさそう
hq = []
ans = 0
for i in range(M):
  for b in jobs[i]:
    heappush(hq, -1 * b)
  if len(hq) > 0:
    m = -1 * heappop(hq)
    ans += m

print(ans)