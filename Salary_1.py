from sys import argv

path, hours, hour_rate, bonus = argv
print(hours, hour_rate, bonus)
hours = int(hours)
hour_rate, bonus = map(float, argv[2:])
# print(type(hours), type(hour_rate), type(bonus))


def salary_calc():
    result = (hours * hour_rate) + bonus
    return result


print(salary_calc())
