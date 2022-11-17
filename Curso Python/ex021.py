#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

somaidade = 0
mulh = 0
maior = 0
nomev = 0
for c in range(1, 5):
    print('----- {}ª PESSOA -----' .format(c))
    nome = str(input('Nome: ')).strip().upper()
    idade =  int(input('Idade: '))
    sexo =  str(input('[M/F]')).strip().upper()
    somaidade += idade
    if c == 1 and sexo in 'Mn':
        maior = idade
        nomev = nome
    if sexo in 'Mn' and idade > maior:
        maior = idade
        nomev = nome
    if idade < 20 and sexo in 'F':
        mulh = mulh + 1
print('No total são {} mulheres com menos de 20 anos' .format(mulh))
media = somaidade/c
print('A média de idade é {}' .format(media))
print('O homem mais velho tem {} e se chama {}' .format(maior, nomev))
