from os import system, name
from time import sleep

def divisao(x,y):

    if y == 0:
        return f'Divisão não por zero'
    return x / y

opcao = {
    1: lambda x,y: x + y,
    2: lambda x,y: x - y,
    3: lambda x,y: x * y,
    4: divisao,
    5: lambda x,y: x ** y,
    6: lambda *args: exit()

}

def limpa():

    if name == 'nt':
        system('cls')
    else:
        system('clear')

def menu():

    while True:
        limpa()
        print('-'*32)
        print('\n')
        print(f'1 - Adição        \n'\
              f'2 - Subtração     \n' \
              f'3 - Multiplicação \n' \
              f'4 - Divisão       \n' \
              f'5 - Potenciação   \n' \
              f'6 - Sai           \n'
              )
        op = int(input('Escolha a sua opção: '))

        if op == 6:
            break

        x, y = input('Entre com os dois numeros utilizando o formato x,y: ').split(',')
        x, y = float(x), float(y)

        
        if op in opcao.keys():
            print(opcao[op](x,y))
            sleep(3)
        else:
            print('Opção inválida !!')
            sleep(1)


if __name__ == '__main__':
    menu()
