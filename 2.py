class ErrorDivisionZero(Exception):
    def __init__(self, txt):
        self.txt = txt


try:
    a = int(input("Делимое:"))
    b = int(input("Делитель:"))
    if b == 0:
        raise ErrorDivisionZero("На ноль делить нельзя")

except ErrorDivisionZero as err:
    print(err)
else:
    print(f"Частное: {a/b}")

