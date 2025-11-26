
#merge two lists and sort the results

list1 = [34,56,12,54,33,232]
list2 = [13,22,32,53,67, 54]

merged_list = list1 + list2
merged_list.sort()
print(merged_list)


#merge two lists without duplicates and sort the results

def merge_lists_no_duplicates(l1, l2):
    merged = list(set(l1 + l2))
    merged.sort()
    return merged

print(merge_lists_no_duplicates(list1, list2))  
