# Основное меню программы
import functions

def menu():
    while True:
        ml = ['1.создать папку','2.создать файл','3.удалить (файл/папку)','4.копировать (файл/папку)','5.просмотр содержимого рабочей директории',
        '6.посмотреть только папки','7.посмотреть только файлы','8.просмотр информации об операционной системе','9.создатель программы',
        '10.играть в викторину','11.мой банковский счет','12.смена рабочей директории','13.выход']
        print('-'*15)
        print(f'{ml[0]}\n{ml[1]}\n{ml[2]}\n{ml[3]}\n{ml[4]}\n{ml[5]}\n{ml[6]}\n'
              f'{ml[7]}\n{ml[8]}\n{ml[9]}\n{ml[10]}\n{ml[11]}\n{ml[12]}')
        print('-'*15)

        choice = input('Выберите пункт меню: ')
        if choice == '1':
            functions.create_directory(input('Введите название папки: ')) 
        elif choice == '2':
            name = input('Введите название файла: ')
            expansion = input('Введите расширение файла: ')
            functions.create_file(name, expansion)
        elif choice == '3':
            text = input('Введите что хотите удалить папку/файл: ').lower()
            name = input('Введите название: ').lower()
            functions.del_directory(text, name)
        elif choice == '4':
            text = input('Введите что хотите копировать папку/файл: ').lower()
            name = input(f'Введите имя {text}, который хотите копировать: ')
            new_name = input('Введите новое имя: ')
            functions.copy_dir_file(text, name, new_name)
        elif choice == '5':
            functions.dir_cont()
        elif choice == '6':
            functions.only_papka()
        elif choice == '7':
            functions.only_files()
        elif choice == '8':
            functions.os_info()
        elif choice == '9':
            functions.creator()
        elif choice == '10':
            functions.viktorina_quiz()
        elif choice == '11':
            functions.account_bank()
        elif choice == '12':
            functions.smena_papki(name = input('Введите путь директории: '))
        elif choice == '13':
            break
