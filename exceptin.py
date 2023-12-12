
try:
    a =  ord('a')
    print(a)
except ValueError:
    print("Can'nt convert")
except ZeroDivisionError:
    print("Error: Can't print by zero")
finally:
    print("Successfully  Run value :%d " %a)
a = 'abcd'
for i in a:
    data = i.split()
    for i in data:
        print(ord(i))
