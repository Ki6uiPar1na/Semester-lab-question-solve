from math import*
def prime_number(n):
    if n <= 1:
        return False
    else:
        for i in range(2, (int(sqrt(n)) + 1)):
            if n % i == 0:
                return False
        return True
for i in range(1, 10001):
    if(prime_number(i)):
        print(i, end=' ')