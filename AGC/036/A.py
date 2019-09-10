S = int(input())
MOD = 10 ** 9
x1, y1, x2, y2 = 0, 0, MOD, 1
y3 = S // MOD
if S % MOD != 0:
  y3 += 1
x3 = x2 * y3 - S

print("{} {} {} {} {} {}".format(x1, y1, x2, y2, x3, y3))