import os


def viewfiles():
    print('ВЫДАЧА СОДЕРЖИМОГО')
    print('---- ---- ---- ----')
    basefile = open("kh.txt", "r")
    content = basefile.read()
    contlist = content.split('\n')
    symb_limit = 49152
    symb_amount = 0
    # print(contlist)
    for k in range(0, len(contlist)):
        if k != len(contlist) - 1:
            if k % 2 == 0:
                if contlist[k+1] == "ПУСТОЙФАЙЛ":
                    print(contlist[k], '  ', 'ПУСТ')

                else:
                    print(contlist[k], '  ', len(contlist[k + 1]))
                symb_amount += len(contlist[k])
            else:
                pass
                symb_amount += len(contlist[k])
        else:
            pass
            symb_amount += len(contlist[k])

    print('---- ---- ---- ----')
    print('ОКТАД СВОБОДНО:', symb_limit - symb_amount)



def makefile():
    filepr = input('ВВЕДИТЕ НАЗВАНИЕ ФАЙЛА (БЕЗ РАСШИРЕНИЯ) ')
    filepr = filepr.upper()
    create = True
    filepr += '.ТЕКСТ'
    basefile = open("kh.txt", "r")
    content = basefile.read()
    contlist = content.split('\n')
    for k in range(0, len(contlist)):
        if k % 2 == 0:
            if filepr == contlist[k]:
                create = False
            else:
                pass
        else:
            pass
    if create is False:
        print('')
        print('УЖЕ СУЩЕСТВУЕТ. ПОПРОБУЙТЕ ДРУГОЕ НАЗВАНИЕ.')
        print('')
    else:
        basefile = open("kh.txt", "a")
        basefile.write('\n' + filepr + '\n')
        basefile.write('ПУСТОЙФАЙЛ')


def readfile():
    basefile = open("kh.txt", "r")
    content = basefile.read()
    contlist = content.split('\n')
    ins = input('ВВЕДИТЕ НАЗВАНИЕ ФАЙЛА БЕЗ РАСШИРЕНИЯ ')
    ins += '.ТЕКСТ'
    check = False
    lnnm = 0
    for k in range(0, len(contlist)):
        if ins == contlist[k]:
            check = True
            lnnm = k
        else:
            pass
    if check is True:
        if contlist[lnnm + 1]:
            if contlist[lnnm + 1] != 'ПУСТОЙФАЙЛ':
                print(contlist[lnnm + 1])
            else:
                print('')
        else:
            print('ПРОГРАММНАЯ ОШИБКА. КОД 54-107')
    else:
        print('НЕ СУЩЕСТВУЕТ.')


def handle_input():
    inp = input('')
    if inp == "ПРОСМ":
        viewfiles()
        handle_input()
    elif inp == "СОЗД":
        makefile()
        handle_input()
    elif inp == "ПРОЧТ":
        readfile()
        handle_input()
    elif inp == "ДОБАВ":
        write_to_file()
        handle_input()
    else:
        print('КОМАНДА НЕ РАСПОЗНАНА')
        handle_input()

while True:
    handle_input()
