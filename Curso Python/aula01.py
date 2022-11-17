nome = str(input('Qual seu nome? '))
if nome == 'Gilson':
    print('Que nome bonito!')
elif nome == "Pedro" or nome == "Maria":
    print('Seu nome é bem popular!')
else:
    print('Seu nome é bem normal')
print('Tenha um bom dia {}!' .format(nome))