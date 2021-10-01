"""
    Parte 2 - Logística

Uma unidade de aplicação precisa receber mais ampolas de vacinas dado o seu estoque baixo, porém ela só
tem K caminhões para buscar o produto com o fornecedor. Considere que cada caminhão consegue carregar até 
100 ampolas mas o galpão do fornecedor é uma bagunça e eles embalaram caixas que podem conter
de 1 até 100 ampolas.

Crie uma função que receba a quantidade K de caminhões disponíveis e a lista de caixas que o fornecedor 
tem para serem carregadas, ou seja, a quantidade de ampolas por caixa, e retorne se os caminhões conseguirão trazer todas as ampolas ou não. Caso não seja possível retorne a lista das unidades que não serão transportadas. Caso seja possível retorne como estão organizadas as caixas por caminhão, isto é, a lista de caixas que cada um está levando.

"""
# Desenvolvido por Paulo Eduardo Caram Guedes
# Data de modificação: 01/10/2021

from os import system, name
from time import sleep

def limpa():
    
    if name == 'nt':
        system('cls')
    else:
        system('clear')


def logistica(qtdCaminhoes, listaCaixas):
    # Declaracao de variaveis
    listaTrucks = [] # Guarda as caixas no caminhao (Guardar Lista, cada lista é um caminhão)
    qtdCaixasTrucks = [] # Lista que guarda a quantidade de ampolas
    sobra_ampolas = 0 # Quantidade ampolas que sobraram
    #retornoTrucks = True # Retorna se a quantidade de caminhoes suporta carregar as ampolas ou não
    soma = 0 # Soma as ampolas - usado para controlar as ampolas por caminhao
    ordenaLista = sorted(listaCaixas, reverse=True)
    total_ampolas = sum(ordenaLista) # Total de ampolas em todas as caixas


    for item in range(0,len(ordenaLista)):

        soma += ordenaLista[item]

        if soma <=100:
            qtdCaixasTrucks.append(ordenaLista[item])
        else:
            listaTrucks.append(qtdCaixasTrucks)
            qtdCaixasTrucks = []
            qtdCaixasTrucks.append(ordenaLista[item])
            soma = ordenaLista[item]

            
    # Fim do for


    if len(qtdCaixasTrucks) !=0:
        listaTrucks.append(qtdCaixasTrucks)

    flag = 0 # Utilizado para fazer slice Lista de caixas que sobraram
    
    for linha in range(0,len(listaTrucks)):
        if qtdCaminhoes >= linha+1:
            print(f'Caminhão{linha+1}', end=" -> ")
        
        for col in range(0,len(listaTrucks[linha])):
            if qtdCaminhoes >= linha+1:
                print(f'\nAmpolas p/ caixa: {listaTrucks[linha][col]}')
                flag +=1
            
        print('='*32)
            

    return  f'Caminhoes enviados: {qtdCaminhoes}\n' \
            f'Caminhoes Necessários para carregas todas as ampolas:  {len(listaTrucks)}\n' \
            f'Cxs que sobraram: {listaTrucks[flag-1:]}'
                   

               
caixas = [10,100,40,55,65,100,88,77,11,8,1,4] # Estoque de cx no fornecedor

while True:
    #limpa() - para utilizar em arquivo .py
    
    try:
        qtd_trucks = int(input('Digite a quantidade de caminhoes (0-Sai): '))
        
    except ValueError:
        print('Somente números !!!')
        sleep(1)
    else:
        if qtd_trucks == 0:
            break
            
        print(logistica(qtd_trucks, caixas)) # Chama a função que coloca as caixas nos caminhoes
        #sleep(3) - para utilizar fora do jupyter
