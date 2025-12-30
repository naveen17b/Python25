
""" 
frozenset: An immutable version of set in Python. 
A frozenset cannot be modified after its creation, making it hashable and suitable for use as a dictionary key or set element.
"""

x = frozenset({1, "apple", True})
print(type(x))  # Output: <class 'frozenset'>

y = frozenset([2, 3, 4, 5])
print(type(y))  # Output: <class 'frozenset'>

# Demonstrating that frozensets are immutable
try:
    x.add(10)  # This will raise an AttributeError
except AttributeError as e:
    print("Error:", e)  # Output: Error: 'frozenset' object has no attribute 'add'

# Using frozensets as dictionary keys
frozenset_dict = {frozenset({1, 2}): "value1", frozenset({3, 4}): "value2"}
print(frozenset_dict)  # Output: {frozenset({1, 2}): 'value1', frozenset({3, 4}): 'value2'} 

# Demonstrating set operations with frozensets
a = frozenset({1, 2, 3})
b = frozenset({3, 4, 5})
print("Union:", a | b)            # Output: Union: frozenset({1, 2, 3, 4, 5})
print("Intersection:", a & b)     # Output: Intersection: frozenset({3