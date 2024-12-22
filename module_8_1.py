def add_everything_up(a, b):
    try:
        result = a + b
        return f'Данные корректны и мы получили результат {round(result, 1)}, округленный до десятых'

    except TypeError as exc:
        result = str(a) + str(b)
        return (f'Ошибка типа - {exc}.\n'
                f'Данные не корректны, разные типы данных.\n'
                f'Поэтому переведем в строковый тип данных str) и получим {result}.\n')


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
