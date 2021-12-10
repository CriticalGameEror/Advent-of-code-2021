f = open("input.txt", "r")
numbers = f.readlines()
f.close()


for x in range(len(numbers)):
    numbers[x] = int(numbers[x])


# total = 0
# previous = None
# for number in numbers:
#     if previous == None:
#         pass
#     elif int(number) > int(previous):
#         total += 1
#     previous = int(number)
    

# print(total)

total = 0
currentSum = 0
previousSum = numbers[0] + numbers[1] + numbers[2]
for x in range(1, len(numbers) - 2):
    currentSum = numbers[x] + numbers[x+1] + numbers[x+2]
    if currentSum > previousSum:
        total += 1
    previousSum = currentSum

print(total)