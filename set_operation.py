a_set = {1, 2, 3, 4, 5}
b_set = {2, 3, 4, 5, 6}
b_set.add(8)
print(b_set)
print(a_set | b_set) #set union
print(a_set & b_set) #set intersection
print(a_set - b_set) #set difference (only a set elements will be exits)
print(a_set ^ b_set) #symmetric difference (same element is remove)
