n = int(input("Enter the year: "))
if n % 400 == 0:
    print("This is leap year")
elif n % 100 != 0 and n % 4 == 0:
    print("This is leap year")
else:
    print("This is not leap year")