# Основное меню программы
import functions
import calculator_generator

def menu():
    while True:
        ml = ['1.создать папку','2.создать файл','3.удалить (файл/папку)','4.копировать (файл/папку)','5.просмотр содержимого рабочей директории',
        '6.посмотреть только папки','7.посмотреть только файлы','8.просмотр информации об операционной системе','9.создатель программы',
        '10.играть в викторину','11.мой банковский счет','12.смена рабочей директории','13.перейти в директорию выше',
        '14.сохранить содержимое рабочей директории в файл', '15.калькулятор', '16.генератор случайных чисел', '17.выход']
        print('-'*15)
        print(f'{ml[0]}\n{ml[1]}\n{ml[2]}\n{ml[3]}\n{ml[4]}\n{ml[5]}\n{ml[6]}\n'
              f'{ml[7]}\n{ml[8]}\n{ml[9]}\n{ml[10]}\n{ml[11]}\n{ml[12]}\n{ml[13]}\n{ml[14]}\n{ml[15]}\n{ml[16]}')
        print('-'*15)

        choice = input('Выберите пункт меню: ')
        if choice == '1':
            functions.create_directory(input('Введите название папки: ')) 
        elif choice == '2':
            name = input('Введите название файла: ')
            expansion = input('Введите расширение файла: ')
            functions.create_file(name, expansion)
        elif choice == '3':
            text = input('Удалить ФАЙЛ - введите 1 или файл, удалить ПАПКУ - 2 или папка: ').lower()
            name = input('Введите название: ').lower()
            functions.del_directory(text, name)
        elif choice == '4':
            text = input('Копировать ФАЙЛ - введите 1 или файл, копировать ПАПКУ - 2 или папка: ').lower()
            name = input('Введите название: ')
            new_name = input('Введите новое название: ')
            functions.copy_dir_file(text, name, new_name)
        elif choice == '5':
            print(functions.dir_cont())
        elif choice == '6':
            print(functions.only_papka())
        elif choice == '7':
            print(functions.only_files())
        elif choice == '8':
            print(functions.os_info())
        elif choice == '9':
            print(functions.creator())
        elif choice == '10':
            functions.viktorina_quiz()
        elif choice == '11':
            functions.account_bank()
        elif choice == '12':
            functions.smena_papki(name = input('Введите путь директории: '))
        elif choice == '13':
            functions.papka_up()
        elif choice == '14':
            functions.save_dir()
        elif choice == '15':
            calculator.calculator()
        elif choice == '16':
            calculator.random_number_generator()
        elif choice == '17':
            break
