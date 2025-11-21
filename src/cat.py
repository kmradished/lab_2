import os
from lg import lg

def cat(p='s'):
    try:
        if os.path.isdir(p):
            print(f"cat: {p}: Это каталог")
            lg(f'cat {p}', False)
            return
        with open(p, 'r', encoding='utf-8') as content:
            content=content.read()
            print(content)
    except FileNotFoundError:
        print(f'cat: {p}: Нет такого файла или каталога')
        lg(f'cat {p}', False)
    except Exception as a:
        print(f'Ошибка: {a}')
        lg(f'cat {p}', False)
    except:
        print('ОШИБКА')
        lg(f'cat {p}', False)