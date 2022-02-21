li = [8, 6, 5, 5, 3, 2]  # 1ый вариант (долго не могла найти ошибку в 1м варианте, поэтому пыталась придумать 2ой. Есть ли способ проще?
print(li)
num = int(input("Введите число:"))
for i in range(len(li)):

    if li[i] == num:
        li.insert(i + 1, num)
        break
    elif li[0] < num:
        li.insert(0, num)
    elif li[-1] > num:
        li.append(num)
    elif li[i] > num and li[i + 1] < num:
        li.insert(i + 1, num)

print(li)

num = int(input("Введите число: "))  # 2ой вариант
li = [8, 5, 4, 4, 2]
print(li)
c = li.count(num)

for element in li:
    if c > 0:
        li.insert(li.index(num) + c, num)
        break
    else:
        if num > element:
            li.insert(li.index(element), num)
            break
        elif num < li[len(li) - 1]:
            li.append(num)
print(li)
