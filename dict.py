my_dict = {'apple': 5, 'banana': 2, 'orange': 8, 'grape': 3}
key_list = list(my_dict.keys())
print(key_list)
# key_list.sort()
print(key_list)
for i in key_list:
    print(f"Key = {i} and value = {my_dict[i]}")