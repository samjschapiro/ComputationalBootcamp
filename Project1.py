import math as m

# problem 1 - Newton's method for computing square roots - "average damping"

def square_root(num, guess):
    iterations = 0
    xNext = 0
    solution = False
    while (solution is False and iterations <= 10):
        iterations += 1
        xNext = 0.5 * (guess + num/guess)
        print(xNext)
        guess = xNext
        if (xNext is m.sqrt(num) is 0):
            solution is True

            
square_root(592, 26)

# problem 2

def collatz_conjecture(n):
    iterations = 0
    while (n != 1):
        if (n % 2 == 0):
            n = n /2
            iterations += 1
        elif (n % 2 != 0):
            n = (3 * n) + 1
            iterations += 1
    return iterations

print("it takes " + str(collatz_conjecture(20)) + " steps to reach 0")

def find_top_collatz_conjecture(start, end):
    max = 0
    index_of_max = 0
    for i in range (start, end):
        if (collatz_conjecture(i) > max):
            max = collatz_conjecture(i)
            index_of_max = i
    return index_of_max

print(find_top_collatz_conjecture(2, 20))

# problem 3

def fibonacci_resursively(n):
    print(1)
