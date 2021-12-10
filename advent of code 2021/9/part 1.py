f = open("input.txt")
inputList = f.readlines()  
f.close()

for row in range(len(inputList)):
  inputList[row] = inputList[row].strip() 

lowStuff = []

for y in range(len(inputList)):
  for x in range(len(inputList[y])):
    # check up
    if y != 0:
      if not(inputList[y-1][x] > inputList[y][x]):
        continue
    # check right
    if x != len(inputList[y]) - 1:
      if not(inputList[y][x+1] > inputList[y][x]):
        continue
    # check down
    if y != len(inputList) - 1:
      if not(inputList[y+1][x] > inputList[y][x]):
        continue
    # check left
    if x != 0:
      if not(inputList[y][x-1] > inputList[y][x]):
        continue
    lowStuff.append(inputList[y][x])

sum = 0
for number in lowStuff:
  sum += int(number) + 1

print(sum)
