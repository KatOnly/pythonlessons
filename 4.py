li = input("Введите слова:").split()

for i, word in enumerate(li, 1):

    if len(word) > 10:
        word = word[0:10]
    print(i, word)
