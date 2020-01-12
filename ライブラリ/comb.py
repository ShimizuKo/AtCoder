N = 100
MOD = 10 ** 9 + 7
#変にエラー吐かれないようにするための変数↑

kai1 = [1, 1]
kai2 = [1, 1]
inverse = [0, 1]
for i in range(2, N + 1):
  kai1.append((kai1[-1] * i) % MOD)
  inverse.append((-inverse[MOD % i] * (MOD // i)) % MOD)
  kai2.append((kai2[-1] * inverse[-1]) % MOD)

def comb(n, r):
  if r < 0 or r > n:
    return 0
  r = min(r, n - r)
  return (kai1[n] * kai2[r] * kai2[n - r]) % MOD