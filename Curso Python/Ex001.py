casa = float(input('Valor do Imóvel: R$ '))
salario = float(input('Qual seu salário? '))
anos = int(input('Em quanto anos deseja financiar?'))
parcela = casa / (anos*12)
print('para pagar um casa de R$ {:.2f} em {} anos' .format(casa, anos))
print('A parcela será de R$ {:.2f}!' .format(parcela))
if parcela <= salario*30/100:
    print('Parabéns, emprestimo aprovado')
else:
    print('Emprestimo recusado')
