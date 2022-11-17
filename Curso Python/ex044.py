'''Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final,
mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.'''

lista = []
for c in range(0, 5):
    lista.append(int(input(f'Digite um valor para posição {c+1}: ')))
print(f'você digitou os valores {lista}', end=' ')
print(f'\nO maior valor digitado foi {max(lista)} nas posições ', end='')
for i, v in enumerate(lista):
    if v == max(lista):
        print(i+ 1, end='... ')
print(f'\nO menor valor digitado foi {min(lista)} nas posições ', end='')
for i, v in enumerate(lista):
    if v == min(lista):
        print(i+ 1, end='... ')
print('\nFim...')
