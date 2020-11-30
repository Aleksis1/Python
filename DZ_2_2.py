# 2.Реализовать обмен значений соседних элементов.

A = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
s = 0
for i in range(int(len(A) / 2)):
    A[s], A[s + 1] = A[s + 1], A[s]
    s += 2
print(A)

A = int(input("Введите необходимое количество чисел (после ввода нажать ENTER): "))
my_list = []
i = 0
s = 0
while i < A:
    my_list.append(input("Введите по одному числу (после ввода нажать ENTER): "))
    i += 1
for i in range(int(len(my_list) / 2)):
    my_list[s], my_list[s + 1] = my_list[s + 1], my_list[s]
    s += 2
print(my_list)
