import os
from ls import ls
from cd import cd
from cat import cat
from cp import cp
from mv import mv
from rm import rm

def main():
    while True:
        current_dir=os.getcwd()
        s=input(f'{current_dir}>>> ').split()

        if not s:
            continue
        if s:
            commanda=s[0]
            match commanda:
                case 'ls':
                    if len(s)>1:
                        ls(' '.join(s[1:]))
                    else:
                        ls('.')
                case 'cd':
                    if len(s)>1:
                        cd(s[1])
                    else:
                        cd('~')
                case 'cat':
                    if len(s)>1:
                        cat(s[1])
                    else:
                        print('ОШИБКА: Не указан файл')
                case 'cp':
                    op=''
                    for i in s:
                        if i =='-r':
                            op=i
                    if len(s)>2:
                        cp(op,s[1], s[2])
                    else:
                        print('неверное кол-во')
                case 'mv':
                    if len(s)==3:
                        mv(s[1], s[2])
                    elif len(s)==2:
                        print(f"mv: после '{s[1]}' пропущен операнд, задающий целевой файл")
                    else:
                        print('введено лишние')
                case 'rm':
                    op=''
                    for i in s:
                        if i=='-r':
                            op='-r'
                    if len(s)>1:
                        rm(op, s[1])
                    else:
                        print('Ошибка с кол-вом')
                case 'exit':
                    break

if __name__=='__main__':
    main()