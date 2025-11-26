
#average of the list of items

def average_of_list(items):
    if len(items) == 0:
        return 0
    return sum(items)/ len(items)

list = [10, 20, 33, 40, 50]
print(average_of_list(list))  