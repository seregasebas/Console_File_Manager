"""
Программа "Личный счет"
Описание работы программы:
Пользователь запускает программу у него на счету 0
Программа предлагает следующие варианты действий
1. пополнить счет
2. покупка
3. история покупок
4. выход
1. пополнение счета
при выборе этого пункта пользователю предлагается ввести сумму на сколько пополнить счет
после того как пользователь вводит сумму она добавляется к счету
снова попадаем в основное меню
2. покупка
при выборе этого пункта пользователю предлагается ввести сумму покупки
если она больше количества денег на счете, то сообщаем что денег не хватает и переходим в основное меню
если денег достаточно предлагаем пользователю ввести название покупки, например (еда)
снимаем деньги со счета
сохраняем покупку в историю
выходим в основное меню
3. история покупок
выводим историю покупок пользователя (название и сумму)
возвращаемся в основное меню
4. выход
выход из программы
"""

import json
import os

# функция сохранения данных в json
def save_json(data, name, opening_mode = 'w'):
    with open(name, opening_mode) as f:
        json.dump(data, f)
       
def bank_acc():
    cash = 0
    purchase = {}
    cash_file = 'cash.json'
    purchase_file = 'purchase.json'

    if os.path.exists(cash_file):
        with open(cash_file, 'r') as f:
            cash = json.load(f)
    
    if os.path.exists(purchase_file):
        with open(purchase_file, 'r') as f:
            for key,value in json.load(f).items():
               purchase[key] = value 

    while True:
        print('+'*15)
        print('Выберите пункт меню:\n1. пополнение счета\n2. покупка\n3. история покупок\n4. остаток средств\n5. выход')
        print('-'*15)
        choice = input()
        if choice == '1':
            cash += (int(input('введите сумму пополнения: '))) #прибавляем введенное число, чтобы баланс был актуален и не обнулялся при каждом запуске
        elif choice == '2':
            price = int(input('введите сумму покупки:' ))
            if  price > cash:
                print('денег не хватает')
            else:
                purchase[(input('ввести название покупки: '))] = price
                cash -= price
        elif choice == '3':
            for key, value in purchase.items():
                print(f'покупка: {key} стоимость: {value}')
        elif choice == '4':
            print(f'на вашем счете: {cash}')
        elif choice == '5':
            save_json(cash, 'cash.json')
            save_json(purchase, 'purchase.json')
            break

bank_acc()