def throw(name):
    print(f"{name} throws the ball")

throw("Krishna")

#def -> is a keyword used to define a function
#throw -> is the name of the function

# function to add two numbers
# a, b are parameters
# 5,9 are arguments, when we call the function and assign the value to the paraments it is know as arguments
def add(a,b):
    return a+b

print(add(5.9,9))


# in pyhton we dont specify the types fot parameters in the function definition

'''
def add(a: int, b: int) -> int:
    return a + b
print(add(5, 9))
# This is a type hint, it is not enforced by the interpreter
'''

