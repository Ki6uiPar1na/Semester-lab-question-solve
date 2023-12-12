r = int(input("Enter the number of rows: "))
c = int(input("Enter the number of columns: "))

# Initialize matrices A, B, and result
A = []
B = []
result = []

# Input elements for matrix A
print("Enter elements for Matrix A:")
for i in range(r):
    temp = []
    for j in range(c):
        num = int(input(f"Enter element at position ({i + 1}, {j + 1}): "))
        temp.append(num)
    A.append(temp)

# Input elements for matrix B
print("\nEnter elements for Matrix B:")
for i in range(r):
    temp = []
    for j in range(c):
        num = int(input(f"Enter element at position ({i + 1}, {j + 1}): "))
        temp.append(num)
    B.append(temp)

# Display matrices A and B
print("\nMatrix A is:")
for i in range(r):
    for j in range(c):
        print(A[i][j], end=" ")
    print()

print("\nMatrix B is:")
for i in range(r):
    for j in range(c):
        print(B[i][j], end=" ")
    print()

# Calculate the sum of matrices A and B
for i in range(r):
    temp = []
    for j in range(c):
        temp.append(A[i][j] + B[i][j])
    result.append(temp)

# Display the matrix sum
print("\nMatrix Sum is:")
for i in range(r):
    for j in range(c):
        print(result[i][j], end=" ")
    print()
