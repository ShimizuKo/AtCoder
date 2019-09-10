N = int(input())
H = list(map(int, input().split()))

ans = "Yes"
H_max = H[0]
for i in range(1, N):
  if H[i] < H_max:
    if H_max - H[i] >= 2:
      ans = "No"
      break
  H_max = max(H_max, H[i])
print(ans)