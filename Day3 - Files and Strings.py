# files and strings

# exercise1

file = open('clients.txt')
data = file.readlines()
list = []
for n in range(0, len(data)):
    line = data[n]
    parts = line.split(" ")
    firstNameFlag = True
    firstName = ""
    lastNameFlag = True
    lastName = ""
    ageFlag = True
    age = 0
    phoneNumFlag = True
    phoneNum = ""
    for n in range(0, len(parts)):
        if (parts[n] == ''):
            continue
        elif (firstNameFlag):
            firstName = parts[n]
            firstNameFlag = False
        elif (lastNameFlag):
            lastName = parts[n]
            lastNameFlag = False
        elif (ageFlag):
            age = int(parts[n])
            ageFlag = False
        elif (phoneNumFlag):
            phoneNum = parts[n].replace("\n", "")
            phoneNumFlag = False
    tuple = (firstName, lastName, age, phoneNum)
    list.append(tuple)

file.close()


# exercise2_1
def sortById(data, column_id):
    return sorted(data, key = lambda tup: tup[column_id])

print(sortById(list, 0))

# exercise2_2
def sortByName(data, column_name):
    tuple = data[0]
    if (column_name == "first name"):
        return sortById(data, 0)
    elif (column_name == "last name"):
        return sortById(data, 1)
    elif (column_name == "age"):
        return sortById(data, 2)
    elif (column_name == "phone number"):
        return sortById(data, 3)

print(sortByName(list, "age"))

# exercise 3
f = open('people.age.txt', 'w')
sorted_data = sortByName(list, "age")
for n in range(0, len(sorted_data)):
    line = sorted_data[n]
    f.write('{} {} {} {}\n'.format(*line))

f.close()
