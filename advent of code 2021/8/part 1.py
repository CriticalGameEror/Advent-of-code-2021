f = open("input.txt")
inputList = f.readlines()
f.close()

for item in range(len(inputList)):
    inputList[item] = inputList[item].split("|")

for collection in range(len(inputList)):
    for item in range(len(inputList[item])):
        inputList[collection][item] = inputList[collection][item].strip().split()

# 1: 2, 4: 4, 7: 3, 8: 7

sum = 0
for collection in inputList:
    for item in collection[1]:
        leng = len(item)
        if leng == 2 or leng == 4 or leng == 3 or leng == 7:
            sum += 1

print(sum)


