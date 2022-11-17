'''Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).'''

soma =  cont = 0
parar = False
while not parar:
    n = int(input('Digite um número ou [999 para parar]: '))
    cont += 1
    soma += n
    if n == 999:
        parar = True
        soma -= 999
print('Você digitou {} números e a soma deles é igual a {}.' .format(cont, soma))
