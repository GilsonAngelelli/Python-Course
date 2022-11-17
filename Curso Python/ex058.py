'''Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.'''

from datetime import datetime
pessoa = {}
pessoa['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
pessoa['idade'] = datetime.now().year - nasc 
pessoa['ctps'] = int(input('Cardeira de trabalho (0 = não possui): '))
if pessoa['ctps'] != 0:
    pessoa['contratacao'] = int(input('Ano de contratação: '))
    pessoa['salario'] = int(input('Salario R$: '))
    pessoa['aposentadoria'] = pessoa['idade'] + ((pessoa['contratacao'] +35) - datetime.now().year )
print('-=' * 30)
for k, v in pessoa.items():
    print(f'  - {k} tem o valor {v}')


