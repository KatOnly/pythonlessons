class NotNumber(Exception):
    def __init__(self, txt):
        self.txt = txt


counter = 1
my_list = []
print('Введите числа по одному, для выхода введите "stop":')
while True:
    try:
        value = input(f"{counter}: ")
        counter += 1
        if value == 'stop':
            break
        if not value.isdigit():
            raise NotNumber("Не число!")
        my_list.append(float(value))
    except NotNumber as err:
        print(err)
print(my_list)
