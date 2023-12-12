a = {'a':2, 'f':3, 'b':6}
print(a)
b = a.keys()
c = list(b)
c.sort()
print(c)
for i in c:
    print(a[c])