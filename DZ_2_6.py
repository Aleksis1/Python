# 6.* Реализовать структуру данных
goods = []
features = {'name-наименование': '', 'price-цена': '', 'quantity-количество': '', 'unit-единица измерения': ''}
analytics = {'name-наименование': [], 'price-цена': [], 'quantity-количество': [], 'unit-единица измерения': []}
num = 0
while True:
    if input('для выхода нажмите Q, \n Enter - продолжить... ').upper() == 'Q':
        break
    num += 1
    for f in features.keys():
        user_data = input(f'{f}: ')
        features[f] = int(user_data) if (
                    f == 'name-наименование' and f == 'price-цена' and f == 'quantity-количество' and f == 'unit-единица измерения') else user_data
        analytics[f].append(features[f])
    goods.append((num, features.copy()))
    print('Текущая аналитика по товарам:\n')
    for key, value in analytics.items():
        print(key, value)
