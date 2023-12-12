
def amstrong(n):
    sum = 0
    temp = n
    while n != 0:
        sum = sum + ((n % 10) ** 3)
        n = n // 10
    if(sum == temp):
        return True
    else:
        return False
    print(sum)
n = 153
if amstrong(n):
    print(1)
else:
    print(2)