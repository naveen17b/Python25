
#give a list of numbers, print the second largest number

def second_largest_number(numbers):
    unique_numbers = list(set(numbers))
    unique_numbers.sort()
    if(len(unique_numbers)<2):
        return None
    return unique_numbers[-2]

print(second_largest_number([42, 19, 33, 31, 91, 29]))  
