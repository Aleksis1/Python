# 4. Реализовать перенос, нумерацию и отсечение.

line = input("Введите строку из нескольких слов: ")
words = line.split()
for i, word in enumerate(words, start=1):
    print(i, word[:10])

my_str_1 = input("Введите строку из нескольких слов: ")
re = my_str_1.split()
for i, re in enumerate(re, start=1):
    print(i, re[:9])
