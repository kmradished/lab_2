import os
from datetime import datetime
from lg import lg

def ls(p='.'):
    try:
        s=p.split()
        current_dir = '.' #текущий директорий
        t=False
        
        for i in s:
            if i == '-l':
                t=True
            else:
                current_dir = i
        sp=os.listdir(current_dir) #список файлов и папок в заданном директории

        if t:
            print(f'Итого {len(sp)}')
            for i in sp:
                if i[0]=='.':
                    continue
                else:
                    metadata=os.stat(os.path.join(current_dir, i))
                    size=metadata.st_size 
                    time=datetime.fromtimestamp(metadata.st_mtime).strftime('%Y-%m-%d %H:%M')
                    print(f'{size} {time} {i}')
        else:
            for i in sp:
                if i[0]=='.':
                    continue
                else:
                    print(i)
        lg(f'ls {p}')
    except FileNotFoundError:
        print(f"ls: невозможно получить доступ к '{p}': Нет такого файла или каталога")
        lg(f'ls {p}', False)
    except Exception as a:
        print(f'Ошибка: {a}')
        lg(f'ls {p}', False)
