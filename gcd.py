a = int(input())
b = int(input())
mn = min(a, b)
while True:
    if a % mn == 0 and b % mn == 0:
        print(mn)
        break
    else:
        mn -= 1 