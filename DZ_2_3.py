# 3. Реализовать время года.

seasons_list = ['зима', 'весна', 'лето', 'осень']
seasons_dict = {1: 'зима', 2: 'Весна', 3: 'лето', 4: 'осень'}
seasons_zone = ("Ждешь тринадцатую зарплату?")
seasons_none = ("И сколько же у тебя времен года?")
month = int(input("Введите число месяца: "))
if month == 12 or month == 1 or month == 2:
    print(seasons_list[0])
    print(seasons_dict[1])
elif month == 3 or month == 4 or month == 5:
    print(seasons_list[1])
    print(seasons_dict[2])
elif month == 6 or month == 7 or month == 8:
    print(seasons_list[2])
    print(seasons_dict[3])
elif month == 9 or month == 10 or month == 11:
    print(seasons_list[3])
    print(seasons_dict[4])
elif month == 13:
    print(seasons_zone)
elif month > 13:
    print(seasons_none)
