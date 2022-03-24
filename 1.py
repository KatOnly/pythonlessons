f = open("test.txt", "w+", encoding="utf-8")
newline = input("Введите данные: \n")
f.writelines(newline + "\n")
while newline:
    newline = input("Введите данные: \n")
    f.writelines(newline + "\n")
    if not newline:
        break
f.close()

f = open("test.txt", "r", encoding="utf-8")
text = f.read().split("\n")
print(text)
f.close()
