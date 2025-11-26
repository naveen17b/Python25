# Remove duplicates from a list

def remove_duplicates(input_list):
    return list(set(input_list))    

sample_list = [1, 2, 2, 3, 4, 4, 5]
print(remove_duplicates(sample_list))  # Output: [1, 2, 3,