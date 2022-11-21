number = int(input("Enter a number: "))
for i in range(1, number+1):
  for j in range(1, i+1):
    print(j, end="")
  print("\r")
for k in range(number+1, 1, -1):
  for l in range(1, k-1):
    print(l, end="")
  print("\r")
for w in range(number+1, 1, -1):
  for x in range(1, w-1):
    print(x, end="")
  print("\r")
for y in range(1, number+1):
  for z in range(1, y+1):
    print(z, end="")
  print("\r")