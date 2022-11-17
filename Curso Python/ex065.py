from random import randint
def sort(lista):
    print('Sorteando')
    for cont in range(0,5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n}', end = ' ')
    print()
def spar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma +=valor
    print(f'A soma dos valores pares foi de {soma}')

        
num = list()
sort(num)
spar(num)


