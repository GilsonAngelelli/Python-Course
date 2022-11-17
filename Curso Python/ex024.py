'''Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''

num1 = float(input('Primeiro valor: '))
num2 = float(input('Segundo valor: '))
opção = 0
while opção != '5':
    print('-=' * 30)
    print('''[ 1 ] SOMAR
[ 2 ] MULTIPLICAR
[ 3 ] MAIOR
[ 4 ] NOVOS NÚMEROS
[ 5 ] SAIR DO PROGRAMA''')
    print('-=' * 30)
    opção = str(input('Qual é a opção >>>  ')).strip()
    if opção == '1':
        soma = num1 + num2
        print('A soma entre {} e {}é igual a {}.'.format(num1, num2, soma))
    elif opção == '2':
        produto = num1 * num2
        print('O produto entre {} e {} é {}.'.format(num1, num2, produto))
    elif opção == '3':
        if num1 > num2:
            maior = num1
        else:
            maior = num2
            print('Entre {} e {} o maior é {}.'.format(num1, num2, maior))
    elif opção == '4':
        print('Informe os numeros novamente:')
        num1 = float(input('Primeiro valor: '))
        num2 = float(input('Segundo valor: '))
    elif opção == '5':
        print('Finalizando')
    else:
        print('Opção invalida, tente novamente')
print('FIM DO PROGRAMA')