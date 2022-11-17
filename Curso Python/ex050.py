'''Faça um programa que leia nome e peso de várias pessoas,                 guardando tudo em uma lista. No final,Mostre: 
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.'''

pessoas = []
temp = []
resp = 0
cont = 0
mais = menos = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(int(input('Peso: ')))
    if len(pessoas) == 0:
        mais = menos = temp[1]
    else:
        if temp[1] > mais:
            mais = temp[1]
        if temp[1] < menos:
            menos = temp[1]
    pessoas.append(temp[:])
    temp.clear()
    cont += 1
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
    
print(f'Foram cadastradas {cont} pessoas.')
print(f'O maior peso foi de {mais} KG', end = ' ')
for p in pessoas:
    if p[1] == mais:
        print(f'{p[0]}', end =' ')
print(f'\nO menor peso foi de {menos} KG', end =' ')
for p in pessoas:
    if p[1] == menos:
        print(f'{p[0]}', end =' ')
print('fim')



