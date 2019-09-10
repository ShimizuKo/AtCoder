N = int(input())
A = []

for _ in range(N):
  a = list(map(int, input().split()))
  A.append([x - 1 for x in a])

ans = 0
cnt = 0 #消化した試合数
M = N * (N - 1) // 2 #最大試合数
while cnt < M:
  tmp = cnt
  q = [i for i in range(N)] #今日の対戦可能者
  while len(q) > 0:
    p = q.pop(0)
    if len(A[p]) == 0:
      continue

    #消化可能な試合があれば, cnt+=1, qから対戦する選手を消去, Aからも該当試合を消去 
    if A[A[p][0]][0] == p and A[p][0] in q:
      q.remove(A[p][0])
      A[A[p][0]].pop(0)
      A[p].pop(0)
      cnt += 1
  if tmp == cnt: #1試合も進まない日があった場合、不可能
    ans = -1
    break
  else:
    ans += 1
print(ans)