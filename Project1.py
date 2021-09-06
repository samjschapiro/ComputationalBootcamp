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

def fibonacci_while(num):
    iterations = 0
    n = 0
    n_minus_2 = 1
    n_minus_1 = 1
    while (iterations < (num-2)):
        n = n_minus_2 + n_minus_1 
        n_minus_2 = n_minus_1 
        n_minus_1 = n 
        iterations += 1
    print(n)

def fibonacci_recursive(n):
   if n <= 1:
       return n
   return(fibonacci_recursive (n-2)+fibonacci_recursive(n-1))


fibonacci_while(7)

print(fibonacci_recursive(7))

# problem 4 - function of form Ax^n + B

def simpsons_rule(a, b, function_A, function_A_degree, function_B): 
    function_of_a = function_A * (a ** function_A_degree) + function_B
    function_of_ab_over2 = function_A * ( ( (a + b) / 2) ** function_A_degree) + function_B
    function_of_b = function_A * (b ** function_A_degree) + function_B
    return (b-a)/6.0 * (function_of_a + 4 * function_of_ab_over2 + function_of_b)

print(simpsons_rule(1, 3, 3, 2, 1)) # integral of 3x^2 + 1 from 1 to 3

# problem 5 

def efficient_modulo(a, n, m):
    if (n % 2 == 0):
        return ((a ** (n/2)) ** 2) % m
    elif (n % 2 != 0):
        return (a * ((a ** (n-1)) ** 2)) % m

print(efficient_modulo(3, 4, 10))