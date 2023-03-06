f = open("input.txt")
inputList = f.readlines()
f.close()


def checkRow(board, used):
    for row in board:
        complete = True
        for number in row:
            useBreak = True
            for thing in used:
                if number == thing:
                    useBreak = False
                    break
            if useBreak == True:
                complete = False
                break
        if complete == True:
            return True
    return False
           

def checkColumn(board, used):
    for x in range(len(board)):      
        complete = True
        for y in range(len(board[x])):         
            useBreak = True
            for thing in used:
                if board[y][x] == thing:
                    useBreak = False
                    break
            if useBreak == True:
                complete = False
                break
        if complete == True:
            return True
    return False

def findScore(board, bruh, used):
    sum = 0
    for row in board:
        for number in row:
            doAdd = True
            for thing in used:
                if number == thing:
                    doAdd = False
                    break
            if doAdd == True:
                sum += int(number)
    print(sum * int(bruh))


numberChoose = inputList.pop(0).strip().split(",")

boards = []
x = -1
for line in inputList:
    if line == "\n":
        boards.append([])
        x += 1
        continue
    boards[x].append(line.strip().split(" "))

for x in range(len(boards)):
    for y in range(len(boards[x])):
        while "" in boards[x][y]:        
            if "" in boards[x][y]:
                boards[x][y].remove("")
            

usedNumbers = []

for number in numberChoose:
    usedNumbers.append(number)
    for x in range(len(boards)): 
        if (checkRow(boards[x], usedNumbers)):
            print(usedNumbers)
            findScore(boards[x], number, usedNumbers)
            exit()
        if (checkColumn(boards[x], usedNumbers)):
            findScore(boards[x], number, usedNumbers)
            exit()



    


