#Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

termo = int(input('Qual o primeiro termo? '))
razão = int(input('Qual a Razão? '))
decimo = + (10 - 1) * razão
for c in range(termo, decimo + razão, razão):
    print('{}' .format(c), end='- ')
print('ACABOU')
