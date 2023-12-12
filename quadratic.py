import cmath
print("Enter the value of a, b, c : ")
a = int(input())
b = int(input())
c = int(input())
discriminant = cmath.sqrt((b ** 2) - (4 * a * c))
x1 = (-b + discriminant) / (2 * a)
x2 = (-b - discriminant) / (2 * a)
print(x1, x2)