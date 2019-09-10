S = input()
T = input()

R = {chr(i) : -1 for i in range(97, 97 + 26)}
Rd = {chr(i) : -1 for i in range(97, 97 + 26)}

def check(i):
  ret = True
  if R[S[i]] >= 0 and R[S[i]] != ord(T[i]):
    ret = False
  if Rd[T[i]] >= 0 and Rd[T[i]] != ord(S[i]):
    ret = False
  if R[S[i]] < 0:
    R[S[i]] = ord(T[i])
  if Rd[T[i]] < 0:
    Rd[T[i]] = ord(S[i])
  return ret

ans = "Yes"
for i in range(len(S)):
  if not check(i):
    ans = "No"
print(ans)