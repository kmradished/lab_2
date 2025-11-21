import os
import shutil
from lg import lg

def mv(fr, to):
    try:
        shutil.move(fr, to)
        lg(f'mv {fr} {to}')
    except FileNotFoundError:
        print(f"mv: не удалось выполнить stat для'{fr}': Нет такого файла или каталога")
    except Exception as a:
        print(f'ОШИБКА {a}')
    except:
        print('ОШИБКА')