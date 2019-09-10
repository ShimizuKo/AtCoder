N = int(input())
S = input()

ans = 1
while len(S) > 0:
  n = S.count(S[0])
  ans *= n + 1
  S = S.replace(S[0], "")

print((ans - 1) % (10 ** 9 + 7))