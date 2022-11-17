'''Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''

cont = soma = maior = menor = 0
resp = 'S'
while resp in 'Ss':
    n1 = int(input('Digite um número: '))
    cont += 1
    soma += n1
    resp = str(input('Quer continuar [S/N]')).strip().upper() 
    if cont == 1:
        maior = menor = n1
    elif n1 > maior:
        maior = n1
    elif n1 < menor:
        menor = n1
media = soma / cont
print('Você digitou {} número e a média foi {:.2f}' .format(cont, media))
print('O menor termo foi {} e o maior foi {}.' .format(menor, maior))
print('FIM')
