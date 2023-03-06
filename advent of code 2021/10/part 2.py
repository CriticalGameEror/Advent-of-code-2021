f = open("input.txt")
inputList = f.readlines()
f.close()

for x in range(len(inputList)):
    inputList[x] = inputList[x].strip()

listOfOpen = ["(", "{", "[", "<"]
listOfClose = [")", "}", "]", ">"]

listOfCorrupt = []

for line in inputList:
    listofChunks = []
    nextLine = False
    for x in range(len(line)):
        for chunk in range(len(listofChunks)):
            listofChunks[chunk] = listofChunks[chunk] + line[x]
        
        doAppend = True
        for chunk in range(len(listofChunks) - 1, -1, -1):
            if listofChunks[chunk][0] in listOfOpen and listofChunks[chunk][-1] in listOfClose:
                if listOfOpen.index(listofChunks[chunk][0]) == listOfClose.index(listofChunks[chunk][-1]):
                    if listofChunks[-1] == listofChunks[chunk]:
                        listofChunks.pop(-1)
                        doAppend = False
                        break    
                    else:
                        listOfCorrupt.append(inputList.index(line))
                        nextLine = True
                        break
        
        if doAppend and nextLine != True:
            if line[x] in listOfClose:
                listOfCorrupt.append(inputList.index(line))
                nextLine = True
            else:
                listofChunks.append(line[x])

        if nextLine:
            break
        
        doAppend = True

for item in listOfCorrupt:
    inputList[item] = None

totalScores = []

for line in inputList:
    if line == None:
        continue

    listofChunks = []
    for x in range(len(line)):
        for chunk in range(len(listofChunks)):
            listofChunks[chunk] = listofChunks[chunk] + line[x]
        
        doAppend = True
        for chunk in range(len(listofChunks) - 1, -1, -1):
            if listofChunks[chunk][0] in listOfOpen and listofChunks[chunk][-1] in listOfClose:
                if listOfOpen.index(listofChunks[chunk][0]) == listOfClose.index(listofChunks[chunk][-1]):
                    if listofChunks[-1] == listofChunks[chunk]:
                        listofChunks.pop(-1)
                        doAppend = False
                        break 
        
        if doAppend:
            listofChunks.append(line[x])
    
    total = 0
    for length in range(len(listofChunks)):
        
        if listofChunks[-1][0] == "(":
            total = (total * 5)  + 1
        elif listofChunks[-1][0] == "[":
            total = (total * 5)  + 2
        elif listofChunks[-1][0] == "{":
            total = (total * 5)  + 3
        elif listofChunks[-1][0] == "<":
            total = (total * 5)  + 4

        listofChunks.pop(-1)
    
    totalScores.append(total)

print(sorted(totalScores))
print(sorted(totalScores)[int((len(totalScores) + 1) / 2) - 1])
