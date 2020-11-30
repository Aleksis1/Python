# Реализовать в виде функции my_func(x, y).

def my_pow_func(x, y):
    try:
        ans = x ** y
    except TypeError:
        return 'Enter float'
    return ans


print(my_pow_func(8, -1))
