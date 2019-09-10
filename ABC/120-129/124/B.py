N = int(input())
H = list(map(int, input().split()))

cnt = 0
for i in range(N):
  if i == 0:
    cnt += 1
  else:
    high = True
    for j in range(i):
      if H[i] < H[j]:
        high = False
    if high:
      cnt += 1
print(cnt)