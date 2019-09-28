N = int(input())

ans = 0.5
if N % 2 == 1:
  ans = (N // 2 + 1) / N

print(ans)