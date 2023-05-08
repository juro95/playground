import timeit

# functional programming puts the emphasis on using functions to process data
# Pure functions are functions that have no side effects and always return the same output for the same input   
# Pure function
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

num1 = 2
num2 = 3

sum_result = add(num1, num2)
product = multiply(num1, num2)
result = add(sum_result, product)

# Anonymous function / Lambda expression
apply_and_sum = lambda f1, f2, a, b: f1(a, b) + f2(a, b)
result = apply_and_sum(add, multiply, num1, num2)

# Higher-order functions: map, filter, and reduce
numbers = [1, 2, 3, 4, 5]

# Using map with a lambda expression
squares = list(map(lambda x: x ** 2, numbers))

# Using filter with a lambda expression
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

#recursion example
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
#with for loop
def factorial_loop(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
    
print(squares)
print(even_numbers)
print(factorial(5))
#print(factorial(30001)) #recursion error because of the maximum recursion depth exceeded. That is because the recursion depth is limited by the stack size.
# The stack is used to store temporary variables and function calls.
# -> memory management 

#time the factorial function
print(timeit.timeit("factorial(5)", globals=globals(), number=10000))
print(timeit.timeit("factorial_loop(5)", globals=globals(), number=10000))
