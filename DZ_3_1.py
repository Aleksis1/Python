# Реализовать функцию, принимающую два числа (позиционные аргументы)
# выполняющую их деление.

def div(*args):
    try:
        arg1 = int(input("Делимое: "))
        arg2 = int(input("Делитель: "))
        res = arg1 / arg2
    except ValueError:
        return 'Value error'
    except ZeroDivisionError:
        return " НА НОЛЬ ДЕЛИТЬ НЕЛЬЗЯ."
    return res


print(f'Ответ: {div()}')


def my_div(num_1, num_2):
    try:
        num_1, num_2 = float(num_1), float(num_2)
        answer = num_1 / num_2
    except ValueError:
        return 'error', 'ошибка числа'
    except ZeroDivisionError:
        return 'Деление на ноль!'
    return answer


my_div(input('Делимое: '), input('Делитель: '))

print(f'Результат: {my_div()}')
