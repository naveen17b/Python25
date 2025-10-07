
"""
Collection of key-value pairs.
"""

x = {"name": "Praveen", "age": 25}
print(type(x))
print(x)

update = x.update(city = 'Delhi')
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
    "Pride and Prejudice": "Jane Austen"
}

print(books)

print(books["To Kill a Mockingbird"])