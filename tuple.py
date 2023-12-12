s = "this is khairul "
ss = "is"
l = 0
r = len(s)
cn = 0
while l <= r and True:
    pos = s.find(ss, l, r)
    if(pos != -1):
        l += pos + len(ss)
        cn += 1
    else:
        break
print(cn)
    