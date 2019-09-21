H, W, A, B = map(int, input().split())

ans = [[0 for _ in range(W)] for _ in range(H)]

#1行(列)全体の反転について、
#行(列):「小さい方」の数は変わらない
#列(行):「小さい方」の数が１つ増える
#よって、
#1. H行W列の0のみ(または1のみ)で埋められた行列を用意する
#2. A列分反転する
#3. B行分反転する　でOK
#"No"の条件は A > W / 2 or B > H / 2 のみ。制約で省かれているので考慮の必要なし

for i in range(H):
  for j in range(A):
    ans[i][j] = 1

for i in range(B):
  for j in range(W):
    ans[i][j] ^= 1

for i in range(H):
  for j in range(W):
    print(ans[i][j], end = "")
  print()