a, b = map(int, input().split())
if a > b:
  a, b = b, a

ans = ""
for _ in range(b):
  ans += str(a)
print(ans)