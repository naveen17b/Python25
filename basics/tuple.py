
x = (1, "apple", True)
print(type(x))

my_tuple = (1, 2, 3, 2, 2)
print(my_tuple.count(2))


my_tuple = (1, 2, 3, 4)
print(my_tuple.index(3))

my_tuple = (1, 2, 3)
print(len(my_tuple))


my_tuple = (5, 1, 8)
print(min(my_tuple))


my_tuple = (5, 1, 8)
print(max(my_tuple))


my_tuple = (1, 2, 3)
print(sum(my_tuple))

my_tuple = (3, 1, 2)
print(sorted(my_tuple)) 

my_tuple = (0, False, True)
print(any(my_tuple))

my_tuple = (1, True, "hello")
print(all(my_tuple))

my_list = [1, 2, 3]
print(tuple(my_list))

# Membership Testing: Use in and not in to check if an element exists in a tuple.
my_tuple = (1, 2, "apple")
print(2 in my_tuple)       # Output: True
print("banana" not in my_tuple)

# slicing a tuple
my_tuple = (1, 2, 3, 4)
print(my_tuple[1:3])


# concatination
t1 = (1, 2)
t2 = (3, 4)

print(t1 + t2)          # Output: (1, 2, 3, 4)

print(t1 * 2)           # Output: (1, 2, 1, 2)

#  Packing and Unpacking Data --> Tuples support packing and unpacking, making them useful for assigning multiple variables at once.
person = ("Alice", 30, "Engineer")
name, age, profession = person
print(name)  # Output: Alice


fruits = ("apple", "banana", "cherry")
for index, fruit in enumerate(fruits):
    print(index, fruit)

    