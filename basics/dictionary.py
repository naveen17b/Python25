"""
dictionary in python :
Collection of key-value pairs.
"""

x = {"name": "Praveen", "age": 25}
print(type(x))
print(x)

print(x.update(city="vizag"))
print(x)

pop = x.popitem()
print(pop)


"""
books and authors
"""

books = {
    "The Great Gatsby": "F. Scott Fitzgerald",
    "To Kill a Mockingbird": "Harper Lee",
    "1984": "George Orwell",
    "Pride and Prejudice": "Jane Austen",
}

print(books)

print(books["To Kill a Mockingbird"])


""" looping through dictionary """

for key, value in x.items():
    print(f"{key}: {value}")

