# all exercise 1

# exercise1_1
def posOrNeg(integers):
    for n in integers:
        if (n > 0):
            print("positive")
        elif (n < 0):
            print("negative")
        else:
            print("zero")
    
posOrNeg([5, 4, -3, 1, 0, 7, 9])

# exercise1_2
def posOrNeg(integers):
    results = []
    for n in integers:
        if (n > 0):
            results.append("positive")
        elif (n < 0):
            results.append("negative")
        else:
            results.append("zero")
    return results

print(posOrNeg([5, 4, -3, 1, 0, 7, 9]))

# exercise1_3
def sumOfCubes(numbers):
    sum = 0
    for n in numbers:
        sum += n ** 3
    return sum

print(sumOfCubes([1, 2, 3, 4, 5]))

# exercise1_4
def findMax(numbers):
    max = numbers[0]
    for n in numbers:
        if (n > max):
            max = n
    return max

print(findMax([492, 8, 3, -33, 481]))

# exercise1_5
def reverse(list):
    list_reversed = []
    index = len(list) - 1
    while (index >= 0):
        list_reversed.append(list[index])
        index -= 1
    return list_reversed


print(reverse([3, 192, 4910, 1]))
