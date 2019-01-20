
import os
import shutil

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.


def create_dir():
    for i in range(1, 10):
        d = os.path.join(os.getcwd(), 'dir_{}'.format(i))
        try:
            os.mkdir(d)
            print('dir_{}, created '.format(i))
        except FileExistsError:
            print('You already have this file!')


def remove_dir():
    for i in range(1,10):
        d = os.path.join(os.getcwd(), 'dir_{}'.format(i))
        try:
            os.rmdir(d)
            print('dir_{}, removed '.format(i))
        except FileExistsError:
            print('You dont have file to remove!')
            
# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def show_off():
    d = os.path.join(os.getcwd())
    lst = os.listdir(d)
    for i in lst:
        print(i)

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

def copy_file():
    copy_file = __file__ + ' - copy'
    shutil.copy(__file__, copy_file)
