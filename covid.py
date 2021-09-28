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
from os import system, name #Importando o módulo OS (do sistema)
from time import sleep # importando apenas o módulo sleep 
from datetime import date # Importando apenas o módulo date

# Declaracao de variaveis globais devido não o sistema não contemplar armazenamento em meios fisicos.

estoque = {}.fromkeys(['Pfizer','CoronaVac','Astrazeneca'],0) # Dicionario que armazena o Estoque
lista_geral = []  # Lista que armazena os nomes, a vacina, dia e hora

# Funçao que registra as vacinas

def registrarVacina():

    # Aqui estou pegando o estoque atual
    # No incio do programa, antes de entrar com estoque o mesmo fica zerado

    estoque_pfizer = estoque.get('Pfizer')
    estoque_coronavac = estoque.get('CoronaVac')
    estoque_astrazeneca = estoque.get('Astrazeneca')

    hoje = date.today()
    data_br = hoje.strftime('%d/%m/%y')


    while True:
        lista = [] # Uso essa lista para inserir na lista_geral, assim obtenho uma matriz n=linhas e 4 col
        limpa()
        
        print('='*32)
        nome = input('Digite seu nome ou (0 - Sai): ')
        
        if nome == '0':
            break
        
        print(f'Data: {data_br}\n')

        qual_vacina = int(input(f'1. Pfizer \n' \
                            f'2. Coronavac \n' \
                            f'3. Astrazeneca \n'\
                            f'Opcao: '))
        
        lista.append(nome)
        
        if qual_vacina == 1 and estoque_pfizer >0:
            
            lista.append('Pfizer')
            estoque_pfizer -= 1
            
        elif qual_vacina == 2 and estoque_coronavac >0:
            lista.append('CoronaVac')
            estoque_coronavac -= 1
            
        elif qual_vacina == 3 and estoque_astrazeneca >0:
            lista.append('Astrazeneca')
            estoque_astrazeneca -= 1
        else:
            print('\nOpcao invalida ou Vacina em falta')
            continue
            
        
        hora = input('Hora: ')
        

        lista.append(data_br)
        lista.append(hora)
        lista_geral.append(lista)
        
        

    print(lista_geral)
    estoque['Pfizer'] = estoque_pfizer
    estoque['CoronaVac'] = estoque_coronavac
    estoque['Astrazeneca'] = estoque_astrazeneca

# Funcao que insere as vacinas no estoque
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
                
            print('\nIncluido no estoque !!')
            sleep(1)

    
def obterTotalVacinados():
    opcao = 10 # Flag de entrada no loop
    
    while opcao != 0:
        limpa()

        if len(lista_geral) == 0:
            print(f'\nNão temos nenhum vacinado ainda !!')
            sleep(1)
            opcao = 0
            
        else:
            print(f'Total de vacinados: {len(lista_geral)}')

            soma_pfizer = 0
            soma_coronavac = 0
            soma_astrazeneca = 0

            for linha in range(0,len(lista_geral)):
                
                for col in range(0,4):
                    if lista_geral[linha][col] == 'Pfizer':
                        soma_pfizer += 1
                    elif lista_geral[linha][col] == 'CoronaVac':
                        soma_coronavac += 1
                    elif lista_geral[linha][col] == 'Astrazeneca':
                        soma_astrazeneca += 1
                        
            print(f'Total de vacinados com PFIZER.....: {soma_pfizer}\n' \
                f'Total de vacinados com CORONAVAC..: {soma_coronavac} \n' \
                f'Total de vacinados com ASTRAZENECA: {soma_astrazeneca}')
        try:
            opcao = int(input('Digite (0 - Sair): '))

        except ValueError:
            print('\nVálido apenas o (0) para sair!!')
            sleep(1)
            
        


        

          
    

def obterMediaVacinacao():
    pass

def obterQtdDoses():
    
    while True:
        limpa()
        try:
            print('='*32)
            op = int(input(f'1. Pfizer\n' \
                           f'2. CoronaVac\n' \
                           f'3. Astrazeneca\n' \
                           f'4. Todas\n' \
                           f'5. Sai:\n' \
                           f'Escolha a sua opção: '))

        except ValueError:
            print('\n Digite apenas números !!')
            sleep(1)
        else:

            if op == 5:
                break
            elif op == 1:
                print(f'Estoque da Vacina PFIZER: {estoque.get("Pfizer")}')
            elif op == 2:
                print(f'Estoque da Vacina CORONAVAC: {estoque.get("CoronaVac")}')
            elif op == 3:
                print(f'Estoque da Vacina ASTRAZENECA: {estoque.get("Astrazeneca")}')
            elif op == 4:
                print(estoque)
            else:
                print('\n Opção Inválida !!')

            sleep(2)


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