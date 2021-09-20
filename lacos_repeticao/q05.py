#Faça um algoritmo que peça ao usuário um número e imprima todos os
# números de um até o número dado.



num = int(input('Digite um numero inteiro qualquer: '))

contador = 1

while contador <= num:
    print(contador, end=" ")
    contador +=1

print('\n')

