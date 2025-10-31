
'''  Variable Scope in Python  '''

x = 10  # Global variable

def my_func():
    x = 5  # Local variable
    print("Inside function:", x)

my_func()          # Prints 5
print("Outside function:", x)  # Prints 10
