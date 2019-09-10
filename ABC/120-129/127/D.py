N, M = map(int, input().split())
A = list(map(int, input().split()))
BC = [list(map(int, input().split())) for _ in range(M)]

BC.sort(reverse = True, key = lambda x:x[1])

i = 0
cnt = 0
while cnt < N and i < M:
  A.extend([BC[i][1] for _ in range(BC[i][0])])
  cnt += BC[i][0]
  i += 1
A.sort(reverse = True)
l = A[0:N]

print(sum(l))