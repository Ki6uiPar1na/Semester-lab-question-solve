with open('abc.txt', 'r') as file:
    data = file.read()
    with open('destination.txt', 'w') as file2:
        file2.write(data)
with open('destination.txt', 'r') as file:
    data = file.read()
    print(data)
