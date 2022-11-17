from datetime import date
atual = date.today().year
nasc = int(input(' Ano de nascimento: '))
idade = atual - nasc
saldo = 18 - idade
if idade == 18:
    print('Você ja esta na idade de se alistar')
elif idade < 18:
    print('Ainda faltam {} anos para você se alistar!' .format(18-idade))
    print('Seu alistamento será no ano de {}!' .format(date.today().year + saldo))
else:
    print('Já se passaram {} anos do seu alistamento!' .format(idade-18))
    print('Seu alistamento foi no ano de {}.' .format(date.today().year - idade + 18))
    