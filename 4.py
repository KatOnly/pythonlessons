from itertools import count
old_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

new_list = [el for el in old_list if old_list.count(el) == 1]
print("Элементы списка, не имеющие повторений:\n", new_list)
