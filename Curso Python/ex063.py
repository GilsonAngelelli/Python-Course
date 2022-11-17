from time import sleep
def contador(i, f , p):
    
    print(f'Contagem de {i} até {f} de {p} em {p}')
    if p <0:
        p *= -1
    if p == 0:
        p = 1
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end=' ')
            cont +=p
            sleep(0.5)
        print('FIM')
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end=' ')
            cont -=p
            sleep(0.5)
        print('FIM')

#programa principal
contador(20, 1, 2)
contador(1, 20, 2)

ini = int(input('Inicio: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)

