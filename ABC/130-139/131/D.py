N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]

AB.sort(key = lambda x: x[1])

time = 0
ans = "Yes"
for ab in AB:
  time += ab[0]
  if time > ab[1]:
    ans = "No"
    break
print(ans) 