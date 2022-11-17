'''Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.'''
'''Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.'''

matriz = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
spar = maior = simpar = scol = mlin =0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'digite um valor:[{l}, {c}] '))
print('-=' * 35)
for l in range(0, 3):    
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end=' ')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
        else:
            simpar += matriz[l][c]
    print()
for l in range(0,3):
    scol += matriz[l][2]
for c in range(0, 3):
    if c == 0:
        mlin = matriz[1][c]
    elif matriz[1][c] > mlin:
        mlin = matriz[1][c]
print('-=' * 35)
print(f'A soma dos número pares é {spar}')
print(f'A soma dos número impares é {simpar}')
print(f'A soma dos valores da 3ª coluna é {scol}')
print(f'O maior valor da linha 2 foi {mlin}')

