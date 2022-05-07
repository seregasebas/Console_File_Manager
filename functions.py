import os
import sys
import shutil

#Создание папки(директории)
def create_directory(name):
    if not os.path.exists(name):
        os.mkdir(name)
        print(f'Папка {name} создана')
    else:
        print(f'Папка {name} уже существует')

#удаление папки(директории)/файла
def del_directory(text, name):
    if text == 'ф':
        os.remove(name)
        print(f'файл {name} удален')
    elif text == 'п':
        os.rmdir(name)
        print(f'папка {name} удалена')
    
# Копирование папки(директории)/файла
def copy_dir_file(text, name, new_name):
    if text[0] == 'ф':
        shutil.copy(name, new_name)
    elif text[0] == 'п':
        shutil.copytree(name, new_name)

# просмотр содержимого рабочей директории
def dir_cont():
    print(os.listdir())

#- посмотреть только папки;
def only_papka():
    papka = []
    for papki in os.walk("."):
        papka.append(papki)
    print(papka[0][1])

#- посмотреть только файлы;
def only_files():
    file = []
    for filenames in os.walk("."):
        file.append(filenames)
    print(file[0][2])

#- просмотр информации об операционной системе;
def os_info():
    os.name()

#- создатель программы;
def creator():
    os.getlogin()

#- играть в викторину;
viktorina()

#- мой банковский счет;
# bank_account()

#- смена рабочей директории (*необязательный пункт);
def smena_papki(name = input('Введите путь директории: ')):
    os.chdir(name)

# Перейти на 1 директорию вверх
def papka_up():
    os.chdir(os.pardir)
#- выход.

#Так же можно добавить любой дополнительный функционал по желанию.





