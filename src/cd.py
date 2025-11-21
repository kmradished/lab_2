import os
from lg import lg

def cd(p):
    try:
        if p=='..':
            os.chdir('..')
        elif p == '~':
            os.chdir(os.path.expanduser('~'))
        else:
            os.chdir(p)
    except Exception as a:
        print(f'Ошибка: {a}')
        lg(f'cd {p}', False)