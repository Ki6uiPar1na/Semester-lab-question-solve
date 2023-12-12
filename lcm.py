a = int(input("Enter first number: "))
b = int(input("Enter second number : "))
mx = max(a, b)
while True:
    if mx % a == 0 and mx % b == 0:
        print(mx)
        break
    else:
        mx += 1
