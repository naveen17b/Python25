

def get_min_max(numbers):
    return min(numbers), max(numbers)

result = get_min_max([3, 1, 4, 1, 5])
print(result)  # Output: (1, 5)
print(type(result))  # Output: <class 'tuple'>

