s = "this is khairul is is this isthis"
ss = "is"
cn = 0
l = 0
r = len(s)
while True:
    pos = s.find(ss, l , r)
    if(pos != -1):
        cn += 1
        l = pos + len(ss)
    else:
        break
print(cn)