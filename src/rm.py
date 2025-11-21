import os
import shutil
from lg import lg

def rm(op, p):
    try:
        full_path=os.path.abspath(p)
        if full_path == '/' or full_path == os.path.abspath('..'):
            print('ОШИБКА: ЗАПРЕЩЕНО УДАЛЯТЬ КОРНЕВОЙ КАТАЛОГ ИЛИ РОДИТЕЛЬСКИЙ')
            lg(f'rm {p} {op}', False)
            return
        if os.path.isdir(p):
            if op=='-r':
                check=input('y/n\n')
                if check=='y':
                    shutil.rmtree(p)
                    lg(f'rm {p} {op}')
                else:
                    print('Отмена удаления')
            else:
                print(f"rm: невозможно удалить '{p}': Это каталог")
        else:
            os.remove(p)
            lg(f'rm {p} {op}', False)
    except FileNotFoundError:
        print(f"rm: невозможно удалить '{p}': Нет такого файла или каталога")
        lg(f'rm {p} {op}', False)
    except Exception as a:
        print(f'Ошибка: {a}')
        lg(f'rm {p} {op}', False)
    except:
        print('ОШИБКА')
        lg(f'rm {p} {op}', False)