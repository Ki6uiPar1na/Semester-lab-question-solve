n = int(input("Enter a even number of size: "))
A = []
for i in range(n):
    N = int(input(f"Enter {i + 1} element of the list : "))
    A.append(N)

D = []
B = []
C = []

for i in range(n // 2):
    B.append(A[i])
for i in range(n // 2 , n):
    C.append(A[i])

print(B)
print(C)



for i in range(n // 2):
    D.append((B[i] * C[i]))

print(D)