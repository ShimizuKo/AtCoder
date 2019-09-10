N, M = map(int, input().split())

MOD = 10 ** 9 + 7
a = []
flag = True
for i in range(M):
  tmp = int(input())
  if i != 0 and tmp == a[-1] + 1:
    print(0)
    flag = False
    break
  a.append(tmp)

if flag:
  max_dis = 0
  dis = []
  for i in range(len(a)):
    if i == 0:
      dis.append(a[i])
    else:
      dis.append(a[i] - a[i - 1] - 1)
    max_dis = max(max_dis, dis[-1])
  if M == 0:
    max_dis = N
    a.append(-1)
  else:
    max_dis = max(max_dis, N - a[-1])
  
  fib = [1, 1]
  for _ in range(max_dis):
    fib.append((fib[-1] + fib[-2]) % MOD)
  ans = 1
  for d in dis:
    ans = (ans * fib[d - 1]) % MOD
  ans *= fib[N - a[-1] - 1] % MOD
  
  print(ans % MOD)