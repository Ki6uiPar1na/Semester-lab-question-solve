n = int(input("Enter what is the last number of your list: "))
my_list = []

for i in range(0, n + 1):
    if i % 2 == 0:
        my_list.append(i)
sum = 0
print(my_list)
for i in my_list:
    sum += i
print(sum)