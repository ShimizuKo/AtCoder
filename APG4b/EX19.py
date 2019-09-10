def saiten(l, c_cnt, w_cnt):
  for i in range(9):
    for j in range(9):
      if l[i][j] == (i + 1) * (j + 1):
        c_cnt += 1
      else:
        w_cnt += 1
        l[i][j] = (i + 1) * (j + 1)
  return l, c_cnt, w_cnt

A = [list(map(int, input().split())) for _ in range(9)]

correct_count = 0
wrong_count = 0

A, correct_count, wrong_count = saiten(A, correct_count, wrong_count)

for i in range(9):
  for j in range(9):
    print(A[i][j], end = "")
    if j < 8:
      print(" ", end = "")
    else:
      print("")

print(correct_count)
print(wrong_count)