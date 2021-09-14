# Faça um script para somar dois numeros e multiplicar o resultado
# pelo primeiro número

try:
    n1 = float(input('Digite N1: '))
    n2 = float(input('Digite N2: '))
except ValueError:
    print('Aceita apenas números')
else:
    soma = n1 + n2
    multiplica=n1*soma
    print(f'A soma do {n1} + {n2} = {soma:.2f}')
    print(f'A multiplicacao por {soma:.2f} * {n1} = {multiplica:.2f}')
