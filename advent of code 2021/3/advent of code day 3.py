f = open("input.txt")
inputList = f.readlines()
f.close()

for x in range(len(inputList)):
    inputList[x] = inputList[x].strip()


bitLength = len(inputList[0])

# gamma = ""
# epsilon = ""
# for x in range(len(inputList[0])):
#     total0 = 0
#     total1 = 0
#     for binary in inputList:
#         if binary[x] == "0":
#             total0 += 1
#         elif binary[x] == "1":
#             total1 += 1
#     if total0 > total1:
#         gamma = gamma + "0"
#         epsilon = epsilon + "1"
#     else:
#         gamma = gamma + "1"
#         epsilon = epsilon + "0"

# print(int(gamma, base=2) * int(epsilon, base=2))

# check bit 0 means largest occurance and 1 is vice versa
def findLife(inputList, checkBit):
    while len(inputList) != 1:
        for x in range(bitLength):
            array0 = []
            array1 = []
            for binary in inputList:
                if binary[x] == "0":
                    array0.append(binary)
                elif binary[x] == "1":
                    array1.append(binary)
            if len(array0) > len(array1):
                if checkBit == 0:
                    inputList = array0 
                else:
                    inputList = array1
            elif len(array0) <= len(array1):
                if checkBit == 0:
                    inputList = array1 
                else:
                    inputList = array0
            if len(inputList) == 1:
                break
    return int(inputList[0], base=2)

oxygen = findLife(inputList, 0)
co2 = findLife(inputList, 1)

print(oxygen * co2)



