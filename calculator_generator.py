#импорты
import random

# напишем декоратор для вывода
def decorator(func):
    def inner(*arg, **kwarg):
        print('Результат: ')
        result = func(*arg, **kwarg)
        print('-' * 15)
        return result
    return inner

# функция результата по знаку и декоратор
@decorator
def znaki(znak, num_1, num_2):
    if znak == '+':
        res = num_1 + num_2
        print(res)
    elif znak == '-':
        res = num_1 - num_2
        print(res)
    elif znak == '*':
        res = num_1 * num_2
        print(res)
    elif znak == '/':
        # исключение при делении на ноль
        try:
            res = num_1 / num_2
        except ZeroDivisionError:
            print('Таки на ноль не надо делить')
        else:
            print(res)

# оооочень простой калькулятор
def calculator():
    
    start = input('Будем считать на калькуляторе? y/n: ')

    #тернарный оператор
    print('стартую калькулятор') if start[0] == 'y' else print('Ok, приходи в следующий раз))')
    while start[0] == 'y':
        num_1 = int(input('Введите число: '))
        znak = input('введите математический знак + / - *: ')
        num_2 = int(input('Введите число: '))

        znaki(znak, num_1, num_2)
        
        start = input('Продолжаем считать на калькуляторе? y/n: ')

# простой генератор рандомных чисел
def random_number_generator():

    start = input('Будем генерить рандомные числа? y/n: ')
    #тернарный оператор
    print('стартую генератор') if start[0] == 'y' else print('слабак))')

    num_1 = int(input('Введите количество цифр: '))
    num_2 = int(input('Введите диапозон для генерации: '))

    res_random = [random.randint(1, num_1) for i in range(1, num_2+1)]

    print(f'вывожу рандомные числа {res_random}')
