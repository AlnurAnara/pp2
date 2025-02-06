def unique_elems(list):
    unique_list=[]
    for elem in list:
        if elem not in unique_list:
            unique_list.append(elem)
    return unique_list



print(unique_elems([1,1,2,2,3,3,4,4]))

#Write a Python function that takes a list and returns a new list with unique elements of the first list