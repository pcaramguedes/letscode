#Escreva um programa para ler o salário mensal atual de um funcionário
# e o percentual de reajuste. Calcular e escrever o valor do novo salário.


try:
    salario = float(input('Entre com o salario: '))
    reajuste = float(input('Entre com o reajuste (%): '))
except ValueError:
    print('Aceita apenas valor númerico')
else:
    salario_corrigido = salario * (1 + (reajuste/100))
    print(f'Novo salário: {salario_corrigido:.2f}')

