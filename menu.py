# Основное меню программы
import functions

def menu():
    while True:
        ml = ['1.создать папку','2.удалить (файл/папку)','3.копировать (файл/папку)','4.просмотр содержимого рабочей директории',
        '5.посмотреть только папки','6.посмотреть только файлы','7.просмотр информации об операционной системе','8.создатель программы',
        '9.играть в викторину','10.мой банковский счет','11.смена рабочей директории','12.выход']
        print('-'*15)
        print(f'{ml[0]}\n{ml[1]}\n{ml[2]}\n{ml[3]}\n{ml[4]}\n{ml[5]}\n{ml[6]}\n'
              f'{ml[7]}\n{ml[8]}\n{ml[9]}\n{ml[10]}\n{ml[11]}\n')
        print('-'*15)

        choice = input('Выберите пункт меню: ')
        if choice == '1':
            functions.create_directory(input('Введите название папки: ')) 
        elif choice == '2':
            text = input('Введите что хотите удалить папку/файл: ').lower()
            name = input('Введите название: ').lower()
            functions.del_directory(text, name)
        elif choice == '3':
            text = input('Введите что хотите копировать папку/файл: ').lower()
            name = input(f'Введите имя {text}, который хотите копировать: ')
            new_name = input('Введите новое имя: ')
            functions.copy_dir_file(text, name, new_name)
        elif choice == '4':
            functions.dir_cont()
        elif choice == '5':
            functions.only_papka()
        elif choice == '6':
            functions.only_files()
        elif choice == '7':
            functions.os_info()
        elif choice == '8':
            functions.creator()
        elif choice == '9':
            functions.viktorina_quiz()
        elif choice == '10':
            pass
        elif choice == '11':
            functions.smena_papki(name = input('Введите путь директории: '))
        elif choice == '12':
            break
