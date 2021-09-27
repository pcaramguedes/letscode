"""
    Nesta parte do projeto você deverá construir um sistema para realizar o controle da vacinação.
    Você deverá considerar que existem somente os seguintes tipos de vacina: Pfizer, CoronaVac,
    Astrazeneca.
    
    O programa deverá exibir um menu inicial com as seguintes opções:

    1 . Registrar uma vacinação.

        Nesta opção você deverá perguntar:
            O nome da pessoa
            Qual a vacina

        Você deverá salvar além desses dados, o valor do dia e da hora de vacinação.

    2. Adicionar estoque de uma vacina
        Nesta opção você deverá perguntar:
            O nome da vacina
            A quantidade a ser adicionada

    3. Obter número total de vacinados
        Nesta opção você deverá imprimir a quantidade total de vacinados e além disso a quantidade 
        total de vacinados por cada uma das vacinas.

    4. Obter média de vacinação diária
        Nesta opção você deverá imprimir a média diária somando todas as vacinas e além disso a 
        média diária por cada uma das vacinas.

    5. Obter a quantidade atual de doses de um tipo de vacina
        Você deverá imprimir a quantidade restante de doses para cada uma das vacinas.

    6. Fechar programa
    
    Observações:

    Caso a pessoa digite uma opção inválida, a programa deverá imprimir "Opção inválida" 
    e perguntar novamente uma nova opção.



"""
# Programa desenvolvido por Paulo Eduardo Caram Guedes
# Data: 27/09/2021
# Data Modificação: 27/09/2021
# Release 1.0.0
from os import system, name
from time import sleep
estoque = {}.fromkeys(['Pfizer','CoronaVac','Astrazeneca'],0)

def registrarVacina():
    pass

def adicionarEstoque():
    while True:
        limpa()
        try:
            print(f'1. Pfizer  \n' \
                f'2. CoronoVac \n' \
                f'3. Astrazeneca \n' \
                f'4. Sair')
            marca = int(input('Qual vacina (4-Sai)?: '))
            
            if marca == 4:
                break
            elif marca <0 or marca >4:
                print('\nOpcao invalida')
                sleep(1)
                continue
                
            qtd =   int(input('Digite a qtd: '))
            
        
            
            
        except ValueError:
            print('\nSomente números inteiros !!')
            sleep(1)
            
        else:
            
            if marca == 1:
                estoque['Pfizer'] = estoque.get('Pfizer') + qtd
            elif marca == 2:
                estoque['CoronaVac'] = estoque.get('CoronaVac') + qtd
            elif marca == 3:
                estoque['Astrazeneca'] = estoque.get('Astrazeneca') + qtd
            else:
                print('\nOpção inválida !!')
                sleep(1)
                
            print(estoque)
            sleep(1)

    
def obterTotalVacinados():
    pass

def obterMediaVacinacao():
    pass

def obterQtdDoses():
    pass

dicio = {
    1:registrarVacina,
    2:adicionarEstoque,
    3:obterTotalVacinados,
    4:obterMediaVacinacao,
    5:obterQtdDoses
}


def limpa():
    if name == 'nt':
        system('cls')
    else:
        system('clear')

def menu():
    
    while True:
        try:
            limpa()
            print('='*32)
            print(f'1. Registrar uma vacinação.      \n' \
                f'2. Adicionar estoque de uma vacina\n' \
                f'3. Obter número total de vacinados\n' \
                f'4. Obter média de vacinação diária\n' \
                f'5. Obter a quantidade atual de doses de um tipo de vacina\n' \
                f'6. Sair\n'
                )   
            print('='*32)
            print(estoque)
       
            op = int(input('Entra com opção: '))
        
            if op in dicio.keys():
                dicio[op]()
            elif op == 6:
                break
            else:
                print('\nOpção inválida !!!')
                sleep(1)
        except ValueError:
            print('\nApenas números !!')
            sleep(1)
            
        else:
            pass


if __name__ == '__main__':
    menu()