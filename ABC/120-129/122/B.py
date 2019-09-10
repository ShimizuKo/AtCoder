S = input()
tmp = 0
ans = 0
for s in S:
  if s == "A" or s == "C" or s == "G" or s == "T":
    tmp += 1
  else:
    if tmp > ans:
      ans = tmp
    tmp = 0
  if tmp > ans:
    ans = tmp
print(ans)