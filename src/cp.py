import os
import shutil
from lg import lg

def cp(op,fr, to):
    try:
        if os.path.isdir(fr):
            if op=='-r':
                shutil.copytree(fr, to)
            else:
                print(f"cp: не указан -r; пропускается каталог '{fr}'")
        else:
            shutil.copy2(fr, to)
        lg(f'cp {fr} {to} {op}')
    except Exception as a:
        print(f'ОШИБКА: {a}')
        lg(f'cp {fr} {to}', False)