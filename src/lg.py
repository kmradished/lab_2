from datetime import datetime

def lg(command, f=True):
    time=datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    with open ('shell.log', 'a', encoding='utf-8') as lg:
        if f:
            lg.write(f'[{time}] {command}\n')
        else:
            lg.write(f'[{time}] ОШИБКА {command}\n')
