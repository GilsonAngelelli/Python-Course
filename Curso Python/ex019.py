#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date
atual = date.today().year
maior = 0
menor = 0
for c in range(1, 8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu?' .format(c)))
    idade = atual - nasc
    if idade >= 18:
        maior += 1
    else:
        idade < 18
        menor += 1
print('Ao todo temos {} menores de idade!' .format(menor))
print('E também temos {} maiores de idade!'.format(maior))
    
