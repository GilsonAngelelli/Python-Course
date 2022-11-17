from wsgiref.validate import validator


def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mErro Digite um número válido\033[m')
        if ok:
            break
    return valor


n = leiaint(('Digite um númera: '))
print(f'Você digitou o número {n}')