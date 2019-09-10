N = int(input())
AB = []

for _ in range(N):
  ab = list(map(int, input().split()))
  ab.sort()
  AB.append(ab)
AB.sort(key = lambda x: x[0])

cnt = 0
for i in range(N):
  if i == 0:
    cnt += 1
  elif AB[i - 1][0] == AB[i][0] and AB[i - 1][1] == AB[i][1]:
    continue
  else:
    cnt += 1
print(cnt) 