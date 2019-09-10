N, M, X, Y = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

def war(Z):
  for i in range(N):
    if x[i] >= Z:
      return False
  for i in range(M):
    if y[i] < Z:
      return False
  return True

ans = "War"
for i in range(X + 1, Y + 1):
  if war(i):
    ans = "No War"
    break
print(ans)