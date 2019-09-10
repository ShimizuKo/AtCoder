N = int(input())
word_list = []
ans = "Yes"
for i in range(N):
  word = input()
  word_list.append(word)
  if i != 0:
    if not(word[0] == word_list[i - 1][-1] and word_list.count(word) == 1):
      ans = "No"
      break
print(ans)