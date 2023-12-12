n = int(input("Enter your number: "))
sum = 1
if n == 1:
    print('1')
else:
    for i in range(1, n + 1):
        sum = sum * i
    print(sum)