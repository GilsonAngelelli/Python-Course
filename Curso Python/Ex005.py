#Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
#- Média abaixo de 5.0: REPROVADO
#- Média entre 5.0 e 6.9: RECUPERAÇÃO
#– Média 7.0 ou superior: APROVADO
n1 = float(input('Primeira nota: '))
n2 = float(input('segunda nota: '))
m1 = (n1 + n2) / 2
if m1 >= 7:
    print('Sua média é {:.1F}, você está APROVADO!' .format(m1))
elif m1 <= 5:
    print('Sua média é {:.1F}, você está REPROVADO!' .format(m1))
else:
    print('Sua média é {:.1F}, você está de RECUPERAÇÃO!' .format(m1))
