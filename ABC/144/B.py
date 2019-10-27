N = int(input())

num = [i for i in range(1, 10)]

ans = "No"
for n in num:
  if N % n == 0 and N // n <= 9:
    ans = "Yes"
    break
print(ans)