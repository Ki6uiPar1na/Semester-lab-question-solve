n = int(input())
s = ""
while n / 2 != 0:
    s += str(n % 2)
    n //= 2
ss = s[:: -1]
print(ss)