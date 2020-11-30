# 1. Реализовать скрипт проверки типа данных.

my_list = [12, None, -77, 'True', True, 9.5]
my_list1 = ['один', 'bleck', 'gost', 'пять', 1, 0, -1, -9, 'один', 'четыре', 'пять',
            'z = [4, -1, -9, 10]' 'a = {1, 3, 11, 25, 13}']


def my_type(el):
    for el in range(len(my_list)):
        print(type(my_list[el]))
    return


my_type(my_list)


def my_type(el):
    for el in range(len(my_list1)):
        print(type(my_list1[el]))
    return


my_type(my_list1)

print(type(my_list))
print(type(my_list1))

my_dann = ['123', 123, [123], 123.0, False]
for i in my_dann:
    print(type(i))
