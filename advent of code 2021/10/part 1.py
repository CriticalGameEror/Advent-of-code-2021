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
                        listOfCorrupt.append(listofChunks[chunk][-1])
                        nextLine = True
                        break


        if doAppend and nextLine != True:
            if line[x] in listOfClose:
                listOfCorrupt.append(line[x])
                nextLine = True
            else:
                listofChunks.append(line[x])

        if nextLine:
            break
        
        doAppend = True

total = 0
total += 3 * listOfCorrupt.count(")")
total += 57 * listOfCorrupt.count("]")
total += 1197 * listOfCorrupt.count("}")
total += 25137 * listOfCorrupt.count(">")

print(total)

