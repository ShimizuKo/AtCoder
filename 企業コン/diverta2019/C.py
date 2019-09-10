N = int(input())
s_list = [input() for _ in range(N)]

ans = 0
start_B = 0
end_A = 0
B_A = 0
for s in s_list:
  ans += s.count("AB")
  if s[0] == "B" and s[-1] == "A":
    B_A += 1
  elif s[0] == "B":
    start_B += 1
  elif s[-1] == "A":
    end_A += 1

if B_A > 0 and start_B + end_A == 0:
  ans += B_A - 1
else:
  ans += min(start_B, end_A) + B_A

print(ans)