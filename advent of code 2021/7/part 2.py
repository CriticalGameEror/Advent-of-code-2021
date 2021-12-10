f = open("input.txt")
inputList = f.read().split(",")
f.close()

def convertToTrueUsage(fuelUsed):
    return int((fuelUsed * (fuelUsed + 1)) / 2) #gauss formula apparently


for x in range(len(inputList)):
    inputList[x] = int(inputList[x]) 

inputList.sort()

lowestFuel = None
for moveToNumber in range(inputList[0], inputList[-1]):
    sum = 0
    for compareNumb in inputList:
        if compareNumb - moveToNumber < 0:
            sum += convertToTrueUsage(moveToNumber - compareNumb)
        else:
            sum += convertToTrueUsage(compareNumb - moveToNumber)
    if lowestFuel == None:
        lowestFuel = sum
        continue
    if sum < lowestFuel:
        lowestFuel = sum

print(lowestFuel)
