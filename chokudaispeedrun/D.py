N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for ab in AB:
  ans += max(ab[0], ab[1])

print(ans)