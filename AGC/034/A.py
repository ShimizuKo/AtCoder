N, A, B, C, D = map(int, input().split())
S = input()

ans = "Yes"
#岩が2個続いてたらダメ
for i in range(A - 1, max(C, D)):
  if i >= A and S[i] == "#" and S[i - 1] == "#":
    ans = "No"
    break

#途中で追い越しが必要な場合
if D < C:
  #岩無しが何個続いてるかカウント
  cnt = 0
  tmp = 0
  for i in range(B - 2, min(D + 1, N)):#BがDに到着するまでに追い越す
    if S[i] == ".":
      tmp += 1
    else:
      cnt = max(cnt, tmp)
      tmp = 0
  cnt = max(cnt, tmp)
  #岩無しのスペースが3個続かなきゃダメ
  if cnt < 3:
    ans = "No"
print(ans)