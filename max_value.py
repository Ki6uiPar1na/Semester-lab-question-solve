
#using list
# def find_max_value(list):
#     max_value = list[0]
#     for i in list:
#         if(i > max_value):
#             max_value = i
#     return max_value
# my_list = [1, 2, 3, 8, 10, 15, 5]
# max_value = find_max_value(my_list)

#using set
def find_max_value(my_set):
    max_value = next(iter(my_set))
    for i in my_set:
        if i > max_value:
            max_value = i
    return max_value

my_set = {1, 2, 3, 4, 8, 12, 4}
print(find_max_value(my_set))
