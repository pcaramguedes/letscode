#Faça um programa que leia dois números e informe o maior deles.

n1 = float(input('Digite um Numero qualquer...: '))
n2 = float(input('Digite outro numero qualquer: '))

if n1 > n2:
    print(f'{n1} é maior que {n2}')
elif n2 > n1:
    print(f'{n2} é maior qe {n1}')
else:
    print(f'{n1} = {n2}')

