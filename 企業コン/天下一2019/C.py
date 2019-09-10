N = int(input())
S = input()

sum_w = [0]
sum_b = [0]
for i in range(N):
  if S[i] == ".":
    sum_w.append(sum_w[-1] + 1)
    sum_b.append(sum_b[-1])
  else:
    sum_b.append(sum_b[-1] + 1)
    sum_w.append(sum_w[-1])

ans = float("inf")
for i in range(N + 1):
  ans = min(ans, sum_b[i] + sum_w[-1] - sum_w[i])
  
print(ans)
