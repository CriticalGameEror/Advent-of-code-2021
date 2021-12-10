f = open("input.txt")
inputList = f.readlines()  
f.close()

sillyStuff = []
beenTo = []

def checkUp(x, y):
    y -= 1
    if [x,y] in beenTo:
        return
    if y != -1:
      if inputList[y][x] != "9":
        sillyStuff.append(inputList[y][x])
        beenTo.append([x, y])
        checkUp(x, y)
        checkRight(x, y)
        checkLeft(x, y)

def checkLeft(x, y):
    x -= 1
    if [x,y] in beenTo:
        return
    if x != -1:
      if inputList[y][x] != "9":
        sillyStuff.append(inputList[y][x])
        beenTo.append([x, y])
        checkUp(x, y)
        checkLeft(x, y)
        checkDown(x, y)

def checkRight(x, y):
    x += 1
    if [x,y] in beenTo:
        return
    if x != len(inputList[y]):
      if inputList[y][x] != "9":
        sillyStuff.append(inputList[y][x])
        beenTo.append([x, y])
        checkUp(x, y)
        checkRight(x, y)
        checkDown(x, y)

def checkDown(x, y):
    y += 1
    if [x,y] in beenTo:
        return
    if y != len(inputList):
      if inputList[y][x] != "9":
        sillyStuff.append(inputList[y][x])
        beenTo.append([x, y])
        checkDown(x, y)
        checkLeft(x, y)
        checkRight(x, y)

for row in range(len(inputList)):
  inputList[row] = inputList[row].strip() 

lowStuff = []
area = []

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
    lowStuff.append([x, y])

for item in lowStuff:
    y = item[1]
    x = item[0]

    sillyStuff.append(inputList[y][x]) #append the digit found
    beenTo.append([x, y])

    checkDown(x, y)
    checkLeft(x, y)
    checkRight(x, y)
    checkUp(x, y)

    area.append(len(sillyStuff))

    sillyStuff = []
    beenTo = []


area = sorted(area)
print(area[-1] * area[-2] * area[-3])