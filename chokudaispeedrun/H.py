N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]

for ab in AB:
  if ab[0] == ab[1]:
    print(-1)
  else:
    print(abs(ab[0] - ab[1]))