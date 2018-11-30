my_tuple = (0, 1, 2, 3)
print(my_tuple)

my_list = list(my_tuple)

print(my_list)
my_list.insert(0, my_tuple)

print(my_list)
q= set(my_list[0])
my_set = set(my_list[1:])
my_set.update(q)
print(my_set)
