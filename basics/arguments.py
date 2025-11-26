''' Functions with arguments '''


def keyword_argument(name, age=20):
    print(f"Name:{name}")
    print(f"Age:{age}")

keyword_argument("Praveen", 25)
keyword_argument("krish")  # Uses default age 20


''' Arbitrary positional arguments '''

def positional_argument(*args):
    for arg in args:
        print(arg)
positional_argument("apple", "banana", "cherry")


def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3, 4, 5))

print(''' keyword arguments''')

""" Inside the function, kwargs is a dictionary of argument names and values."""

def keyword_arguments(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
keyword_arguments(name="Praveen", age=25, city="Delhi")


print(" *************************************")
print (''' "Example of mixed arguments" ''')

def mixed_arguments(name, age=20, *args, **kwargs):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)
mixed_arguments("Praveen", 25, "apple", "banana", city="Delhi", country="India")
