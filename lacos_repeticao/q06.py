#Faça um programa que peça para o usuário digitar a idade, o salário e o
# sexo de uma pessoa até que as entradas digitadas sejam válidas.

#    Idade: entre 0 e 150;
#    Salário: maior que 0;
#    Gênero: M, F ou Outro.

idade = 151

while (idade <0 or idade > 150):
    idade = int(input('Digite a sua idade: '))


salario = 0
while salario == 0:
    salario = float(input('Digite o seu salario: '))


while True:
    genero = input('Digite o seu sexo: ')
    
    if (genero != 'f' or genero != 'F'):
        print(f'{genero} nao existe, digite novamente ')
        continue


