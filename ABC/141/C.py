N, K, Q = map(int, input().split())

score = [K - Q for _ in range(N)]
for _ in range(Q):
  A = int(input()) - 1
  score[A] += 1

for s in score:
  if s > 0:
    print("Yes")
  else:
    print("No")