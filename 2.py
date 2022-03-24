with open('test2.txt', 'r', encoding='UTF-8') as f:
    lines = f.readlines()
    print(f"Всего строк: {len(lines)}")
    for i, string in enumerate(lines):
        words = string.split()
        print(f"Слов в строке {i + 1}: {len(words)}")




