old_list = [45, 60, 40, 20, 35, 50, 90, 3, 500]
new_list = [el for el in old_list if el > old_list[old_list.index(el)-1]]

print(old_list)
print(new_list)

