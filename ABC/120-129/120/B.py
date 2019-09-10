A, B, K = map(int, input().split())
div = []
for i in range(1, 101):
  if A % i == 0 and B % i == 0:
    div.append(i)
print(div[len(div) - K])