f = open("input.txt")
inputList = f.readlines()
f.close()

beenTo = []

def addUpAll(x, y):
    if y != len(inputList) - 1:
        inputList[y+1][x] += 1
        if inputList[y+1][x] > 9 and [x,y+1] not in beenTo:
            beenTo.append([x,y+1])
            addUpAll(x, y+1)
    if y != 0:
        inputList[y-1][x] += 1
        if inputList[y-1][x] > 9 and [x,y-1] not in beenTo:
            beenTo.append([x,y-1])
            addUpAll(x, y-1)
    if x != 0:
        inputList[y][x-1] += 1
        if inputList[y][x-1] > 9 and [x-1,y] not in beenTo:
            beenTo.append([x-1,y])
            addUpAll(x-1, y)       
    if x != len(inputList) - 1:
        inputList[y][x+1] += 1
        if inputList[y][x+1] > 9 and [x+1,y] not in beenTo:
            beenTo.append([x+1,y])
            addUpAll(x+1, y)
    if x != len(inputList) - 1 and y != len(inputList) - 1:
        inputList[y+1][x+1] += 1
        if inputList[y+1][x+1] > 9 and [x+1,y+1] not in beenTo: 
            beenTo.append([x+1,y+1])
            addUpAll(x+1, y+1)
    if x != 0 and y != len(inputList) - 1:
        inputList[y+1][x-1] += 1
        if inputList[y+1][x-1] > 9 and [x-1,y+1] not in beenTo:
            beenTo.append([x-1,y+1])
            addUpAll(x-1, y+1)
    if x != 0 and y != 0:
        inputList[y-1][x-1] += 1
        if inputList[y-1][x-1] > 9 and [x-1,y-1] not in beenTo:
            beenTo.append([x-1,y-1])
            addUpAll(x-1, y-1)
    if x != len(inputList) - 1 and y != 0:
        inputList[y-1][x+1] += 1
        if inputList[y-1][x+1] > 9 and [x+1,y-1] not in beenTo:
            beenTo.append([x+1,y-1])
            addUpAll(x+1, y-1)
    

for x in range(len(inputList)):
    inputList[x] = list(inputList[x].strip())
    for number in range(len(inputList[x])):
        inputList[x][number] = int(inputList[x][number])

turns = 0
totalNumberCount = len(inputList[0]) * len(inputList)

while True:
    turns += 1

    # increment all by 1
    for y in range(len(inputList)):
        for x in range(len(inputList[y])):
            inputList[y][x] += 1

    while True:
        doBreak = True
        for y in range(len(inputList)):
            for x in range(len(inputList[y])):
                if inputList[y][x] > 9 and [x,y] not in beenTo:
                    doBreak = False
                    beenTo.append([x,y])
                    addUpAll(x, y)
        if doBreak:
            break
        doBreak = True
    
    beenTo = []

    count = 0
    for y in range(len(inputList)):
        for x in range(len(inputList[y])):
            if inputList[y][x] > 9:
                inputList[y][x] = 0
                count += 1
                if count == totalNumberCount:
                    print(turns)
                    exit()

    
