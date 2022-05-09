import os
import sys
import shutil
import viktorina
import bank_account

#Создание папки(директории)
def create_directory(name):
    if not os.path.exists(name):
        os.mkdir(name)
        return f'Папка {name} создана'
    else:
        return f'Папка {name} уже существует'

#Создание файла
def create_file(name, expansion):
    text_f = open(f'{name}.{expansion}', 'w')
    text_f.close()
    return f'файл {name}.{expansion} создан'
    
#удаление папки(директории)/файла
def del_directory(text, name):
    if text[0] == 'ф' or text[0] == '1':
        os.remove(name)
        print(f'файл {name} удален')
    elif text[0] == 'п' or text[0] == '2':
        os.rmdir(name)
        print(f'папка {name} удалена')
    
# Копирование папки(директории)/файла
def copy_dir_file(text, name, new_name):
    if text[0] == 'ф' or text[0] == '1':
        shutil.copy(name, new_name)
        print(f'файл {name} скопирован с новым названием: {new_name}')
    elif text[0] == 'п' or text[0] == '2':
        shutil.copytree(name, new_name)
        print(f'папка {name} скопирована с новым названием: {new_name}')

# просмотр содержимого рабочей директории
def dir_cont():
    return os.listdir()

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
    return os.name

#- создатель программы;
def creator():
    return os.getlogin()

#- играть в викторину;
def viktorina_quiz():
    viktorina.quiz()

#- мой банковский счет;
def account_bank():
    bank_account.bank_acc()

#- смена рабочей директории (*необязательный пункт);
def smena_papki(name):
    os.chdir(name)
    return f'вы в директории: {os.getcwd()}'

# Перейти на 1 директорию вверх
def papka_up():
    os.chdir(os.pardir)
    print(f'вы в директории: {os.getcwd()}')
#- выход.

#Так же можно добавить любой дополнительный функционал по желанию.





