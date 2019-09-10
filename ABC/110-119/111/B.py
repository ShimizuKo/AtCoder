N = int(input())
ABC = [int("{0}{0}{0}".format(i)) for i in range(10)]
for abc in ABC:
  if N <= abc:
    print(abc)
    break