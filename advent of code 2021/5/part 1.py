f = open("input.txt")
inputList = f.readlines()
f.close()

for x in range(len(inputList)):
    inputList[x] = inputList[x].strip().split("->")

for x in range(len(inputList)):
    for y in range(len(inputList[x])):
        inputList[x][y] = inputList[x][y].strip().split(",")

for line in range(len(inputList)):
    for points in range (len(inputList[line])):
        for point in range (len(inputList[line][points])):
            inputList[line][points][point] = int(inputList[line][points][point])
    
points = {}

for lines in inputList:
    x1 = lines[0][0]

    y1 = lines[0][1]

    x2 = lines[1][0]

    y2 = lines[1][1]

    if x1 == x2 and not(y1 == y2):
        if y1 > y2:
            y1, y2 = y2, y1
        for y in range(y1, y2 + 1):
            if (x1, y) not in points:
                points[(x1, y)] = 0
            else:
                points[(x1, y)] += 1
    if y1 == y2 and not(x1 == x2):
        if x1 > x2:
            x1, x2 = x2, x1
        for x in range(x1, x2 + 1):
            if (x, y1) not in points:
                points[(x, y1)] = 0
            else:
                points[(x, y1)] += 1
    else:
        continue
    
sum = 0
for key in points:
    if points[key] >= 1:
        sum += 1

print(sum)