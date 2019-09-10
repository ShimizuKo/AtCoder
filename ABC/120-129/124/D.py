N, K = map(int, input().split())
S = input()

nums = []
now = 1
cnt = 0
for i in range(N):
  if S[i] == str(now):
    cnt += 1
  else:
    nums.append(cnt)
    now = 1 - now
    cnt = 1
if cnt != 0:
  nums.append(cnt)

if len(nums) % 2 == 0:
  nums.append(0)

add = 2 * K + 1

sums = [0 for _ in range(len(nums) + 1)]
for i in range(len(nums)):
  sums[i + 1] = sums[i] + nums[i]

ans = 0
for i in range(len(nums)):
  if i % 2 == 1:
    continue
  
  left = i
  right = min(i + add, len(nums))
  tmp = sums[right] - sums[left]

  ans = max(tmp, ans)

print(ans)