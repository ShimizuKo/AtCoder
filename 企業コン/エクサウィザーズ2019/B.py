N = int(input())
s = input()

red = 0
for si in s:
  if si == "R":
    red += 1
if red > N / 2:
  print("Yes")
else:
  print("No")