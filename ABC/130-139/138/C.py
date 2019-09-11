N = int(input())
v = list(map(int, input().split()))

v.sort(reverse = True)
while len(v) > 1:
  x = v.pop(-1)
  y = v.pop(-1)
  v.append((x + y) / 2)
print(v[0])