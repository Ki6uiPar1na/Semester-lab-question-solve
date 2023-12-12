with open('new.txt', 'w') as file:
    file.write("Khairul")

# with open('new.txt', 'r') as file:
#     content = file.read()
#     print(content)

with open('new.txt', 'a') as file:
    file.write(" Islam tushar")

with open('new.txt', 'r') as file:
    content = file.read()
    print(content)