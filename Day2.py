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

# all exercise 2

# exercise2_1
print("skip")

# exercise2_2
birthdays = [
    ('Connie', 'Sept 4',),
    ('Sam', 'Oct 19'),
    ('Stu', 'Jun 7'),
    ('Sangbum', 'Nov 17')
]

print(sorted(birthdays)) # sorts by first entry in tuple

birthdays_by_date = [
    ('Sept 4', 'Connie'),
    ('Oct 19', 'Sam'),
    ('Jun 7', 'Stu'),
    ('Nov 17', 'Sangbum')
]

print(sorted(birthdays_by_date))

# exercise2_3
numbers = [n for n in range(1, 11)]
numberPairs = []

index = 0
while (index < len(numbers) - 1):
    numberPairs.append("("+str(numbers[index])+", "+str(numbers[index+1])+")")
    index += 1

print(numberPairs)

# exercise2_4
def vectorSum(v1, v2):
    return (v1[0] + v2[0], v1[1] + v2[1])

print(vectorSum((3, 4), (5, -1)))

# all exercise 3

# exercise3_1
days_of_the_week = {
    'Mon' : 1,
    'Tues' : 2,
    'Weds' : 3,
    'Thur' : 4,
    'Fri' : 5,
    'Sat' : 6,
    'Sun': 7
}

days_of_the_week_reversed = {
    1 : 'Mon',
    2 : 'Tues',
    3 : 'Weds',
    4 : 'Thur',
    5 : 'Fri',
    6 : 'Sat',
    7 : 'Sun'
}

print(days_of_the_week)
print(days_of_the_week_reversed)

# exercise3_2
items = ['dog', 'pencil', 'fence', 'dog', 'apple', 'dog', 'dog', 'dog', 'pear', 'pencil', 'pear', 'pear']

counts = dict()
for i in items:
    counts[i] = counts.get(i, 0) + 1

print(counts)

# exercise3_3

tuples = counts.items()
sorted_tuples = sorted(tuples, key = lambda x: x[1], reverse = True)

print(sorted_tuples[0])
print(sorted_tuples[1])

# all exercise 4 

# exercise4_1
def symmetric_dif(s1, s2):
    return (s1 - s2) | (s2 - s1)

A = set([1, 2, 5, 7, 8, 9])
B = set([2, 4, 5, 8, 10])

print(symmetric_dif(A, B))

# exercise4_2
list = [1, 4, 5, 3, 6, 7, 5, 3, 1, 9, 3, 3, 4, 2]

list_to_set = set(list)
print(list_to_set)

# exercise4_3
def allowed_users(users, bad):
    set_users = set(users)
    return set_users - bad

users = ['tom', 'pam', 'sasha', 'jj', 'que', 'jeff']
bad = set(['jeff', 'sasha'])

print(allowed_users(users, bad))