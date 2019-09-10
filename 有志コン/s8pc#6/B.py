N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]

ans = float("inf")
for i in range(N):
  IN = AB[i][0]
  for j in range(N):
    OUT = AB[j][1]
    tmp = 0
    for k in range(N):
      tmp += abs(IN - AB[k][0]) + abs(AB[k][0] - AB[k][1]) + abs(AB[k][1] - OUT)
    ans = min(ans, tmp)
print(ans)