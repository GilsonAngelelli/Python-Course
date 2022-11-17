'''Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.'''

nome = str(input('Digite seu nome: ')).strip().upper()
sexo = str(input('Informe seu sexo: [M/F]: ')).strip().upper()[0]
idade = str(input('Digite sua idade: ')).strip()
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor informe seu sexo: [M/F]: ')).strip().upper()[0]
    while idade not in '0123456789':
        idade = str(input('Digite sua idade: ')).strip()
if  sexo == 'M':
        sexo = 'MASCULINO'
else:
     sexo = 'FEMININO'
print('Seu nome é {}, você é do sexo {} e tem {} anos.' .format(nome, sexo, idade))
