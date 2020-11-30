# Реализовать функцию int_func(), принимающую слово из маленьких латинских букв
# и возвращающую его же, но с прописной первой буквой.

def int_func(text):
    return text.title()


print(int_func('Нихрена не понятно'))
res_int_func = int_func('Полное непонимание')
print(res_int_func)
