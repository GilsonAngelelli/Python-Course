'''Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.'''


num = ((int(input('DIgite um número: '))), (int(input('DIgite um número: '))), (int(input('DIgite um número: '))), (int(input('DIgite um número: '))))
print(f'Voce digitou os valores {num}')
print(f'O valor 9 aparece {num.count(9)}')
if 3 in num:
    print(f'O número 3 apareceu na posição {num.index(3)+1}')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')

