f = open("input.txt")
inputData = f.read().split(",")
f.close()

ages = {-1:0, 0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}

for number in inputData:
    ages[int(number)] += 1

def numbOfFishes(days):
    for length in range(days):
        replaced = None
        for x in range(len(ages) - 2, -2, -1):
            if x == -1:
                ages[8] = ages[x]
                ages[6] += ages[x]
                ages[x] = 0
                continue
            if replaced == None:
                replaced = ages[x-1]
                ages[x-1] = ages[x]
                ages[x] = 0
                continue
            current = replaced
            replaced = ages[x-1]
            ages[x-1] = current
    sum = 0
    for key in ages:
        sum += ages[key]
    return sum

print(numbOfFishes(256))