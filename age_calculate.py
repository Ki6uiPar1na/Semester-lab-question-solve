t = int(input("Enter how many ieteration you want: "))

def age_catagory(n):
    if n >= 0 and n <= 12:
        catagory = "Child"
    elif n >= 13 and n <= 19:
        catagory = "Teenger"
    elif n >= 20 and n <= 59:
        catagory = "Adult"
    elif n < 0:
        catagory = "Age can'nt be negative"
    else:
        catagory = "Senior Citigen"
    return catagory

for i in range(t):
    age = float(input())
    print("Your age catagory is :", age_catagory(age))
