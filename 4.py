dictionary = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

with open('test4.txt', 'r', encoding='UTF-8') as f_en:
    l_en = f_en.read()
l_ru = l_en
for en, ru in dictionary.items():
    l_ru = l_ru.replace(en, ru)

with open('test4_1.txt', 'w', encoding='UTF-8') as f_ru:
    f_ru.write(l_ru)
