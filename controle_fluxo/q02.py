#Faça um código que leia um número e informe se ele é par ou ímpar.

n1 = float(input('Digite um numero qualquer: '))

if (n1%2) == 0:
    print(f'{n1} -> PAR')
else:
    print(f'{n1} -> IMPAR')
