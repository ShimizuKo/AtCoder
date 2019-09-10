N, K = map(int, input().split())
S = list(input())

if S[K - 1] == "A":
  S[K - 1] = "a"
elif S[K - 1] == "B":
  S[K - 1] = "b"
else:
  S[K - 1] = "c"

for s in S:
  print(s, end = "")
print()