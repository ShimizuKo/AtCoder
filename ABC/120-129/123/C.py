N = int(input())
time = [int(input()) for _ in range(5)]

def get_times(n):
  ret = int(N / n)
  if N % n != 0:
    ret += 1
  return ret

cnt = 0
neck = float("inf")
for t in time:
  times = get_times(t)
  times_n = get_times(neck)
  if times > times_n:
    cnt += times - times_n + 1
    neck = t
  else:
    cnt += 1
print(cnt)