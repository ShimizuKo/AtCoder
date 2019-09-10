R, G, B, N = map(int, input().split())

ans = 0
for r in range(int(N / R) + 1):
  for g in range(int((N - r * R) / G) + 1):
    if (N - r * R - g * G) % B == 0:
      ans += 1

print(ans)