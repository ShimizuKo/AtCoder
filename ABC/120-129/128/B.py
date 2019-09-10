N = int(input())
SP = []

for i in range(N):
  S, P = input().split()
  P = int(P)
  SP.append([S, P, i + 1])

SP.sort(key = lambda x:(x[0], -x[1]))

for sp in SP:
  print(sp[2])