a = [1, 2, 3, 4]
even = []
def eve():
    for i in a:
        if i % 2 == 0:
            even.append(i)
        else:
            continue
string = 'Attack'
for i in string:
    a = ord(i);
    a = a + 1;
    print(chr(a), end='')