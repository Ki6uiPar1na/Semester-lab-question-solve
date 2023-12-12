def display_factor(n):
    factor = []
    for i in range(1, n + 1):
        if n % i == 0:
            print(i, end=' ')
n = int(input())
display_factor(n)