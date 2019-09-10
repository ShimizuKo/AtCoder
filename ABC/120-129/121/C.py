N, M = map(int, input().split())
AB = [list(map(int, input().split())) for i in range(N)]
AB.sort()

ans = 0
for i in range(N):
  if AB[i][1] < M:
    ans += AB[i][0] * AB[i][1]
    M -= AB[i][1]
  else:
    ans += AB[i][0] * M
    break
print(ans)