'''Тесты для функций Console_file_manager'''
import os
from viktorina import num_to_str
from functions import os_info, smena_papki, dir_cont, create_file, create_directory, creator

# тест функции преобразования даты в прописное название
# из модуля viktorina.py
# функцию num_to_str перенес как глобальную в модуле 
def test_num_to_str():
    assert num_to_str('15.02.1987') == 'пятнадцатое февраля 1987 года'

# тест функции просмотр информации об операционной системе
# в самой функции изменил print на return
def test_os_info():
    assert os_info() in ('posix, os2, ce, nt, riscos, java')

# тест функции смена директории
# в самой функции изменил print на return
def test_smena_papki():
    assert smena_papki('/Users/sergejvolozin/Desktop/Программер') == 'вы в директории: /Users/sergejvolozin/Desktop/Программер'

# тест функции просмотр содержимого рабочей директории
# в самой функции изменил print на return
def test_dir_cont():
    assert len(dir_cont()) == len(os.listdir())

# тест функции cоздание файла
# в самой функции изменил print на return
def test_create_file():
    assert create_file('text','txt') == 'файл text.txt создан'

# тест функции создатель программы
# в самой функции изменил print на return
def test_creator():
    assert creator() == os.getlogin()


# тест функции Создание папки(директории)
# в самой функции изменил print на return
def test_create_directory():
    if not os.path.exists('new_papka'):
        assert create_directory('new_papka') == 'Папка new_papka создана'
        assert create_directory('new_papka') == 'Папка new_papka уже существует'
    else:
        os.rmdir('new_papka')
        assert create_directory('new_papka') == 'Папка new_papka создана'
        assert create_directory('new_papka') == 'Папка new_papka уже существует'