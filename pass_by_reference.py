def modify(my_list):
    my_list.append(1)
    return my_list
list = [5, 2, 3, 4]
print(list)
list1 = modify(list)
print(list1)
print(list)