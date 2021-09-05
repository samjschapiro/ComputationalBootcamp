## Imports
from math import sqrt, pi, exp

## All Exercise 1


## exercise1_1
exercise1_1 = (1.3/1.2 + 4.3*2.0)/(1.5-2.3)

print(exercise1_1)

## exercise1_2
exercise1_2 = (4431 % 7) == (7523 % 7)

print(exercise1_2)

## exercise1_3
pi = 355/113
circumference = 2 * pi * 5
area = pi * 5**2

print("circumference is: " + str(circumference))
print("area is: " +str(area))
print("pi is: "+str(pi))


## All Exercise 2


## exercise2_1
def isEven(a):
    return a % 2 == 0

print("3 is: "+str(isEven(3)))
print("4 is: "+str(isEven(4)))
print("0 is: "+str(isEven(0)))

## exercise2_2
def absValue(a):
    if (a < 0):
        return a *-1
    else:
        return a

print("the absolute value of -7.5 is: " + str(absValue(-7.5)))
print("the absolute value of 99 is: " + str(absValue(99)))
print("the absolute value of 0 is: " + str(absValue(0)))

## exercise2_3
def square(a):
    return a ** 2

def sumOfSquares(x, y, z):
    return square(x) + square(y) + square(z)

print("the square of -5 is: " + str(square(-5)))
print("the sum of the squares of 3, 4, 5 is: " + str(sumOfSquares(3, 4, 5)))

## exercise2_4
def factorial(a):
    if (a == 1):
        return 1
    return a * factorial(a-1)

print("the factorial of 7 is: " + str(factorial(7)))
print("the factorial of 5 is: " + str(factorial(5)))


## All Exercise 3


## exercise3_1
def squareOfOdd(n):
    sum = 0
    for i in range(0, n+1):
        if (i % 2 != 0):
            sum += square(i)
    return sum

print("the sum of odd squares from 0 to 3 is: " + str(squareOfOdd(3)))
print("the sum of odd squares from 0 to 9 is: " + str(squareOfOdd(9)))

## exercise3_2
def divisibleNaturalNums(n):
    while (n > 0):
        if (n % 3 == 0 and n % 5 == 0 and n % 10 != 0):
            print(n)
        n -= 1

divisibleNaturalNums(100)

## exercise3_3
def printChessBoard():
    for r in range(0, 16):
        if (r % 2 == 0):
            print("B W B W B W B W B W B W B W B W")
        elif (r % 2 != 0):
            print("W B W B W B W B W B W B W B W B")

printChessBoard()

## exercise3_4

def firstTenFibonacci():
    # first two terms
    n1, n2 = 0, 1
    count = 0
    while count < 10:
        print(n1)
        nth = n1 + n2
        # update values
        n1 = n2
        n2 = nth
        count += 1

firstTenFibonacci()

## exercise3_5

def factorialNonRecursive(n):
    result = 1
    while (n > 0):
        result *= n
        n = n - 1
    return result

print("the factorial of 5 is: "+ str(factorialNonRecursive(5)))
