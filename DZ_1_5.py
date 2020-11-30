revenue = float(input('Выручка: '))
costs = float(input('Издержки: '))

result = revenue - costs

if result > 0:
    print('Компания работает с прибылью:', '{:,}'.format(result).replace(',', ' '))
    print("Рентабельность: {}%".format(result / revenue))
    people = int(input('Численность сотрудников: '))
    print(f'прибыль на одного сотрудника: {result / people:.2f}')
elif result < 0:
    print('Компания работает с убытком:', '{:,}'.format(result).replace(',', ' '))
else:
    print('Компания работает в 0' '{:,}'.format(result).replace(',', ' '))

