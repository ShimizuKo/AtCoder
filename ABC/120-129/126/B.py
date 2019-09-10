S = input()

foward = int(S[0 : 2])
back = int(S[2 : 4])

foward_MM = False
back_MM = False

if foward >= 1 and foward <= 12:
  foward_MM = True
if back >= 1 and back <= 12:
  back_MM = True

if foward_MM and back_MM:
  print("AMBIGUOUS")
elif foward_MM and not back_MM:
  print("MMYY")
elif not foward_MM and back_MM:
  print("YYMM")
else:
  print("NA")