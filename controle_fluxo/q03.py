#Faça um programa que receba 3 notas de prova de um aluno,
# calcule a média e diga se ele foi aprovado ou reprovado.
# A média para aprovação é de pelo menos 6 (aprovado se média maior 
#ou igual a 6).


n1 = float(input('Digite N1: '))
n2 = float(input('Digite N2: '))
n3 = float(input('Digite N3: '))

media = (n1+n2+n3) / 3

if media >=6:
    print(f'\nNota={media:.2f} - Aprovado')
else:
    print(f'\nNota={media:.2f} - Reprovado')

