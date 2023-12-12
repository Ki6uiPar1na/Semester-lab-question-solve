r1 = int(input("Enter the number of rows for Matrix A: "))
c1 = int(input("Enter the number of columns for Matrix A: "))

r2 = int(input("Enter the number of rows for Matrix B: "))
c2 = int(input("Enter the number of columns for Matrix B: "))

# Initialize matrices A, B, and result
A = []
B = []
result = []

# Input elements for matrix A
print("Enter elements for Matrix A:")
for i in range(r1):
    temp = []
    for j in range(c1):
        num = int(input(f"Enter element at position ({i + 1}, {j + 1}): "))
        temp.append(num)
    A.append(temp)

# Input elements for matrix B
print("\nEnter elements for Matrix B:")
for i in range(r2):
    temp = []
    for j in range(c2):
        num = int(input(f"Enter element at position ({i + 1}, {j + 1}): "))
        temp.append(num)
    B.append(temp)

# Display matrices A and B
print("\nMatrix A is:")
for i in range(r1):
    for j in range(c1):
        print(A[i][j], end=" ")
    print()

print("\nMatrix B is:")
for i in range(r2):
    for j in range(c2):
        print(B[i][j], end=" ")
    print()

# Check if matrices can be multiplied
if c1 != r2:
    print("\nMatrices can't be multiplied due to incompatible dimensions.")
else:
    # Initialize result matrix for multiplication
    #that's the key code
    for i in range(r1):
        temp = []
        for j in range(c2):
            temp.append(0)
        result.append(temp)
        #that's the key code

    # Perform matrix multiplication
    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                result[i][j] += A[i][k] * B[k][j]

    # Display the matrix product
    print("\nMatrix Product is:")
    for i in range(r1):
        for j in range(c2):
            print(result[i][j], end=" ")
        print()
