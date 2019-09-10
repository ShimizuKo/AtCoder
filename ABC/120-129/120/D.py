#未完成
N, M = map(int, input().split())
A = []
B = []
for i in range(M):
  a, b = map(int, input().split())
  A.append(a - 1)
  B.append(b - 1)
print(A)
print(B)

def search(x, y, num):
  search_list = [[x, y]]
  searched = [[False for i in range(N)] for j in range(N)]
  while len(search_list) > 0:
    print(search_list)
    target = search_list.pop()
    for i in range(num, M):
      if searched[target[0]][target[1]]:
        break
      if A[i] == target[0]:
        if B[i] == target[1]:
          return True
        else:
          search_list.append([B[i], target[1]])
      if B[i] == target[0]:
        if A[i] == target[1]:
          return True
        else:
          search_list.append([A[i], target[1]])
      searched[target[0]][target[1]] = True
  return False


def can_go(num):
  ret = 0
  for i in range(N):
    for j in range(i + 1, N):
      if not search(i, j, num):
        ret += 1
  return ret

for i in range(M):
  print(can_go(i))