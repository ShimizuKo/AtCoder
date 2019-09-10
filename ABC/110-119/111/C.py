n = int(input())
v = list(map(int, input().split()))

e = []
o = []
for i in range(n):
  if i % 2 == 0:
    e.append(v[i])
  else:
    o.append(v[i])

freq_e = {}
freq_o = {}
for j in range(int(n / 2)):
  if (str(e[j]) in freq_e):
    freq_e[str(e[j])] += 1
  elif not(str(e[j]) in freq_e):
    freq_e[str(e[j])] = 1
  if (str(o[j]) in freq_o):
    freq_o[str(o[j])] += 1
  elif not(str(o[j]) in freq_o):
    freq_o[str(o[j])] = 1

freq_e_sorted = sorted(freq_e.items(), key = lambda x: -x[1])
freq_o_sorted = sorted(freq_o.items(), key = lambda x: -x[1])
if freq_e_sorted[0][0] != freq_o_sorted[0][0]:
  ans = n - freq_e_sorted[0][1] - freq_o_sorted[0][1]
elif len(freq_e_sorted) == 1 and len(freq_o_sorted) == 1:
  ans = freq_e_sorted[0][1]
elif len(freq_e_sorted) == 1 or freq_e_sorted[0][1] + freq_o_sorted[1][1] > freq_e_sorted[1][1] + freq_o_sorted[0][1]:
  ans = n - freq_e_sorted[0][1] - freq_o_sorted[1][1]
else:
  ans = n - freq_e_sorted[1][1] - freq_o_sorted[0][1]
print(ans)