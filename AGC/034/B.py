s = input()

abc = s.count("ABC")
cnt = 0
while abc != 0:
  cnt += abc
  s = s.replace("ABC", "BCA")
  abc = s.count("ABC")
print(cnt)