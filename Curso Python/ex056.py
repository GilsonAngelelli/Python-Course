'''Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.'''

aluno = {}

aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input('Média: '))
if aluno["media"] < 7:
    aluno['ar'] = 'Reprovado'
else:
    aluno['ar'] = 'Aprovado'
print('-=' * 40)
print(f'O aluno {aluno["nome"]} teve média {aluno["media"]} e está {aluno["ar"]}')
