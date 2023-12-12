def fibonacci(n):
    a, b = 0, 1
    for i in range(0, n):
        print(a, end=' ')
        a, b = b, a + b

n = 6
fibonacci(n)
