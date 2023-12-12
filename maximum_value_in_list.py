my_list = []


def find_max_value(my_list):
    max_value = my_list[0]
    for i in my_list:
        if i > max_value:
            max_value = i
    return max_value

n = int(input("Enter how many number in your list: "))
for i in range(n):
    num = int(input(f"Enter {i + 1} number: "))
    my_list.append(num)

max_value = find_max_value(my_list)

print("The max value in your list is : ",max_value)
