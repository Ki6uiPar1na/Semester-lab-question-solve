from math import*
def is_prime(n):
    if n <= 1:
        return False
    else:
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

cn = 0
n = int(input("Enter the upper bound: "))
i = 2
prime = []
while True:
    if is_prime(i):
        cn += 1
        prime.append(i)
    if cn == n:
        break
    i += 1
# print(prime)
for i in range(len(prime)):
    print(prime[i], end = ' ')
print()
