def count_report_num(children, x):
  if len(children[x]) == 0:
    return 1
  
  ret = 1
  for i in range(len(children[x])):
    ret += count_report_num(children, children[x][i])
  return ret

N = int(input())
p = [-1]
tmp = list(map(int, input().split()))
for i in range(N - 1):
  p.append(tmp[i])

children = [[] for _ in range(N)]
for i in range(1, N):
  parent =p[i]
  children[parent].append(i)

for i in range(N):
  print(count_report_num(children, i))