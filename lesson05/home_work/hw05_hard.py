# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.

print('sys.argv = ', sys.argv)


def print_help():
    print('help - получение справки')
    print('mkdir <dir_name> - создание директории')
    print('ping - тестовый ключ')
    print('cp <file_name> - создает копию указанного файла')
    print('rm <file_name> - удаляет указанный файл')
    print('cd <full_path or relative_path> - меняет текущую директорию на указанную')
    print('ls - отображение полного пути текущей директории')

def make_dir():
    if not dir_name:
        print('Необходимо указать имя директории 2м параметром')
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))

def copy_file():
    if not dir_name:
        print('Необходимо указать имя файла 2м параметром')
        return
    file_path = os.path.join(os.getcwd(), dir_name)
    shutil.copy(file_path, file_path + ' - copy')
    print('файл {} скопирован'.format(dir_name))

def remove_file():
    if not dir_name:
        print('Необходимо указать имя файла 2м параметром')
        return
    answer = input('Вы действительно хотите удалить файл {}? (Y/N) '.format(dir_name))
    if answer.upper() != 'Y':
        print('Отмена')
        return
    file_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.remove(file_path)
        print('файл {} удалён'.format(dir_name))
    except FileNotFoundError:
        print('файл {} не существует'.format(dir_name))

def change_dir():
    if not dir_name:
        print('Необходимо указать имя файла 2м параметром')
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.chdir(dir_path)
        print('перешли в {}'.format(dir_name))
    except FileNotFoundError:
        print('папки {} не существует'.format(dir_name))

def print_path():
    print(os.getcwd())

def ping():
    print("pong")

do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    'cp': copy_file,
    'rm': remove_file,
    'cd': change_dir,
    'ls': print_path
}

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None


if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")
