# https://www.reddit.com/r/adventofcode/comments/rbvpui/2021_day_8_part_2_my_logic_on_paper_i_used_python/

f = open("input.txt")
inputList = f.readlines()
f.close()

for item in range(len(inputList)):
    inputList[item] = inputList[item].split("|")

for collection in range(len(inputList)):
    for item in range(len(inputList[item])):
        inputList[collection][item] = inputList[collection][item].strip().split()

# 1: 2, 4: 4, 7: 3, 8: 7

largeSum = 0
for combination in inputList:
    keys = {0:"", 1:"", 2:"", 3:"", 4:"", 5:"", 6:"", 7:"", 8:"", 9:""}
    fives = []
    sixes = []
    diff = []
    for item in combination[0]:
        if len(item) == 2:
            keys[1] = item
    for item in combination[0]:    
        if len(item) == 4:
            keys[4] = item
            for letter in item:
                if letter not in keys[1]:
                    diff.append(letter)
    for item in combination[0]:
        if len(item) == 3:
            keys[7] = item
    for item in combination[0]:
        if len(item) == 7:
            keys[8] = item
    for item in combination[0]:
        if len(item) == 5:
            fives.append(item)
    for item in combination[0]:
        if len(item) == 6:
            sixes.append(item)
    
    # check 3
    for item in fives:
        doPop = False
        add = 0
        for letter in item:
            if letter in keys[1]:
                add += 1
                if add == 2:
                    keys[3] = item
                    doPop = True
                    break
        if doPop:
            fives.pop(fives.index(item))
            break
    
    # check 5
    for item in fives:
        doPop = False
        add = 0
        for letter in item:
            if letter in diff:
                add += 1
                if add == 2:
                    keys[5] = item
                    doPop = True
                    break
        if doPop:
            fives.pop(fives.index(item))
            break

    #add two
    keys[2] = fives[0]

    # check 9
    for item in sixes:
        doPop = False
        add = 0
        for letter in item:
            if letter in diff or letter in keys[1]:
                add += 1
                if add == 4:
                    keys[9] = item
                    doPop = True
                    break
        if doPop:
            sixes.pop(sixes.index(item))
            break

    # check 6
    for item in sixes:
        doPop = False
        add = 0
        for letter in item:
            if letter in diff:
                add += 1
                if add == 2:
                    keys[6] = item
                    doPop = True
                    break
        if doPop:
            sixes.pop(sixes.index(item))
            break
    
    # add 0
    keys[0] = sixes[0]

    numbers = ""
    for item in combination[1]:
        for key in keys:
            if sorted(keys[key]) == sorted(item):
                numbers = numbers + str(key)
                break
    largeSum += int(numbers)

print(largeSum)

    
    


        
    

    
    
        
    
        

         




    # sum = ""
    # for item in collection[1]:
    #     sum = sum[item] + sum
    # numbers.append(int(sum))

    


