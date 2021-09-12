# problem 1
def pair_lists(a, b): 
    d = []
    if (len(a) >= len(b)):
        for n in range(0, len(b)):
            tuple = (a[n], b[n])
            d.append(tuple)
    elif (len(a) < len(b)):
        for n in range(0, len(a)):
            tuple = (a[n], b[n])
            d.append(tuple)
    return d

print(pair_lists([1, 2, 3], ['x', 'y', 'z']))
    
# problem 2 - contains with already sorted list

def contains(list, center, value):
    if (len(list) != 1 and value < list[center]):
        lower = []
        for n in range(0, center):
            lower.append(list[n])
        return contains(lower, int(center/2), value)
    elif (len(list) != 1 and value > list[center]):
        upper = []
        for n in range(center+1, len(list)):
            upper.append(list[n])
        return contains(upper, int(center/2), value)
    elif (value == list[center]):
        return True
    elif (value != list[center]):
        return False

print(contains([1, 3, 4, 9, 11, 123, 4190], 3, 1))

# problem 3
def primeNums(n):

    list = []
    for i in range(0, n):
        list.append(True)
    list[0] = False
    list[1] = False

    for p in range(2, (int)(n ** 0.5)):
        if (list[p] is True):
            initial_p = p
            while (p < n):
                if (p == initial_p):  
                    p += initial_p
                    list[p] = False
                else:
                    list[p] = False
                    p += initial_p
    values = []
    for d in range(0, n):
        if (list[d] is True):
            values.append(d)
    return values

print(primeNums(100))

# problem 4 - decomposed tree
def flattenTree(t, root):
    tree = []
    for n in range(0, len(t)):
        if (isinstance(t[n], int)):
            tree.append(t[n])
            root.append(t[n])
        elif (isinstance(t[n], list)):
            tree.append(flattenTree(t[n], root))
    return root

T = [1, 2, [3, 4, 5], 6, [7, [8, 9], 10, [11, [12]], 13], 14]
print(flattenTree(T, []))


# problem 5 - list to dictionary
def listToDictionary(list):
    dict = {}
    for n in range(0, len(list)):
        tuple = list[n]
        dict.__setitem__(tuple[0], tuple[1])
    return dict

print(listToDictionary([ ("Bill", "Apr 1"), ("Ron", "Jun 6"), ("Kat", "May 12"), ("Eric", "Jun 6"), ("Que", "Feb 10") ]))

# problem 6 - skipped; implementation already delineated in project summary
