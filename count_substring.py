string = 'isis is khairul islam tushar is'
sub_string = 'is'
s_len = len(string)
sub_len = len(sub_string)
count = 0
l = 0
r = s_len
while True:
    pos = string.find(sub_string, l, r)
    if pos != -1:
        count += 1
        l += sub_len + pos
    else:
        break
    if l > r:
        break
print(count)