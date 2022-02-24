def my_f(name, surname, date, city, email, phone):
       print(f"{name} {surname}, {date}, {city}, {email}, {phone}")


my_f(name=input("Введите имя: "),
     surname=input("Введите фамилию: "),
     date=input("Введите дату рождения: "),
     city=input("Введите город проживания: "),
     email=input("Введите email: "),
     phone=input("Введите телефон:"))
