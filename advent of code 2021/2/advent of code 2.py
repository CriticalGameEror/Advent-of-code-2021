f = open("input.txt", "r")
inputList = f.readlines()
f.close()

depth = 0
forward = 0
aim = 0

for x in range(len(inputList)):
    inputList[x] = inputList[x].strip().split(" ")

for array in inputList:
    if array[0] == "forward":
        forward += int(array[1])
        depth += aim * int(array[1])
    elif array[0] == "down":
        aim += int(array[1])
    elif array[0] == "up":
        aim -= int(array[1])

print(forward * depth)

