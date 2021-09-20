#Uma empresa irá aplicar um reajuste nos salários de seus funcionários de acordo com
# as seguintes regras:

#Salário até R$2800,00 (incluindo): aumento de 20%;

#Salários entre R 2800,00 e R$7000,00: aumento de 15%;

#Salários entre R 7000,00 e R$15000,00: aumento de 10%;

#Salários de R$15000,00 em diante: aumento de 5%.

#Dado o salário de um funcionário, informe: o salário antes do reajuste; o percentual
#de aumento aplicado; o valor do aumento e o novo salário.

salario = float(input('Digite o Salário: '))
salario_antes_reajuste = salario

if salario >= 15000.00:
    aumento = 0.05
    valor_aumento = salario * aumento
    salario += valor_aumento
elif salario > 7000.00:
    aumento = 0.10
    valor_aumento = salario * aumento
    salario += valor_aumento
elif salario > 2800.00:
    aumento = 0.15
    valor_aumento = salario * aumento
    salario += valor_aumento
else:
    aumento = 0.20
    valor_aumento = salario * aumento
    salario += valor_aumento
print('\n-----------------------------------------')
print(f'Salario antigo: {salario_antes_reajuste:.2f}')
print(f'Perc% Aumento.: {aumento * 100}%')
print(f'Valor Aumento.: {valor_aumento:.2f}')
print(f'Novo Salário..: {salario:.2f}')
print('\n-----------------------------------------')

