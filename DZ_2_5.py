# 5. Реализовать структуру «Рейтинг».

my_list = [7, 5, 3, 3, 2]
print(f"Текущий рейтинг: - {my_list}")
digit = int(input("Результат: "))
el = 1
while digit:
    for el in range(len(my_list)):
        if my_list[el] == digit:
            my_list.insert(el + 1, digit)
            break
        elif my_list[0] < digit:
            my_list.insert(0, digit)
            break
        elif my_list[-1] > digit:
            my_list.append(1)
            break
        elif my_list[el] > digit and my_list[el + 1] < digit:
            my_list.insert(el + 1, digit)
            break
    print(f"Новый рейтинг: - {my_list}")
    digit = int(input("Следующий результат: "))
