
'''  Lambda Functions in Python  
A lambda function is a small anonymous function that can take any number of arguments but can only have one expression.
Syntax:
lambda arguments: expression
'''
# Example 1: A simple lambda function that adds 10 to the input number
add_10 = lambda x: x + 10
print(add_10(5))  # Output: 15

# Example 2: A lambda function that multiplies two numbers
multiply = lambda x,y: x*y
print(multiply(4,78))

# Example 3: Using lambda function with map() to square each number in a list
marks = [57,96,86,97,75]
squared_marks = list(map(lambda x : x**2, marks))
print(squared_marks)  # Output: [3249, 9216, 7396, 9409, 5625]

# Example 4: Using lambda function with filter() to get even numbers from a list
numbers = [1,2,3,4,5,6,7,8,9,10]
even_numbers = list(filter(lambda x: x%2 ==0, numbers))
print(even_numbers)

# Example 5: Using lambda function with sorted() to sort a list of tuples based on the second element
tuples_list = [(1, 'apple'), (3, 'banana'), (2, 'cherry')]
sorted_tuples = sorted(tuples_list, key=lambda x: x[1])
print(sorted_tuples)  # Output: [(1, 'apple'), (3, 'banana'), (2, 'cherry')]


# Example 6: Using lambda function with reduce() to compute the product of a list of numbers

from functools import reduce
numbers = [1,2,3,4]
product = reduce(lambda x,y: x*y, numbers)
print(product)  # Output: 24

# Example 7: Lambda function with no arguments
greet = lambda : "Hello, World!"
print(greet())  # Output: Hello, World!

# Example 8: Lambda function with conditional expression
maximum_value = lambda x,y: x if x>y else y
print(maximum_value(10,20))  # Output: 20

# Example 9: Lambda function returning another function
def make_incrementor(n):
    return lambda x: x + n
increment_by_5 = make_incrementor(5)
print(increment_by_5(10))  # Output: 15

# Example 10: Using lambda function with list comprehension
numbers = [1,2,3,4,5]
doubled_numbers = [(lambda x: x*2) (x) for x in numbers]
print(doubled_numbers)  # Output: [2, 4, 6, 8, 10]]



