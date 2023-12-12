n = 6
cn = 0
cn1 = 0
cn2 = 1
print(cn1, cn2, end=" ")

while True:
    print(cn1 + cn2, end=' ')
    next_term = cn1 + cn2
    cn1 = cn2
    cn2 = next_term
    cn += 1
    if(cn == n - 2):
        break
