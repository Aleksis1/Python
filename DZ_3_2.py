# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя

instructions = input('Введите запрашиваемые данные (для продолжения нажмите Enter).')
surname = input('Ваша Фамилия: ')
name = input('Ваше Имя: ')
middlename = input('Ваше Отчество: ')
year = int(input('Ваша дата рождения (формат ДДММГГГГ): '))
residence = input('Ваше месьто жительства: ')
registration = input('Ваше место регистрации: ')
email = input('Ваша электронная почта: ')
telephone = input('Ваш номер телефона: ')


def personal_info(**kwargs):
    return kwargs


print(personal_info(surname=input('Ваша Фамилия: '),
                    name=input('Ваше Имя: '),
                    middlename=input('Ваше Отчество: '),
                    year=input('Ваша дата рождения (формат ДДММГГГГ): '),
                    residence=input('Ваше месьто жительства: '),
                    registration=input('Ваше место регистрации: '),
                    email=input('Ваша электронная почта: '),
                    telephone=input('Ваш номер телефона: ')
                    ))
