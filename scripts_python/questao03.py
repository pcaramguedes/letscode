#Faça um programa que peça um nome e a idade que a pessoa fez ou vai
# fazer esse ano de 2021. Ao final, informe o ano de nascimento dessa
# pessoa.


try:
    nome = input('Digite o seu nome: ')
    idade = int(input('Qual idade que irá fazer ou fez esse ano: '))
except ValueError:
    print('O campo idade, só aceita números inteiros')
else:
    ano_nascimento = 2021 - idade
    print(f'\n{nome.capitalize()} o seu ano de nascimento:{ano_nascimento}')

