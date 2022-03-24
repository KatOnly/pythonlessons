import re

report = {}
with open('test6.txt', 'r', encoding='UTF-8') as f:
    text = f.read()
    f.seek(0)
    for i in f:
        i = i.split(":")
        hours = re.findall(r"\d+", i[1])
        report.update({i[0]: sum([int(i) for i in hours])})

print(f"Файл:\n{text}\n")
print(f"Словарь:\n{report}")