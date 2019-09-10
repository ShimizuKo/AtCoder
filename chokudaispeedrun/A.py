N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]

for ab in AB:
  print(ab[0] * ab[1])