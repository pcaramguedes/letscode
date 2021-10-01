"""
    Faça uma função que verifique se um valor é perfeito ou não. Um valor é dito perfeito quando ele é igual 
    a soma dos seus divisores excetuando ele próprio. (Ex: 6 é perfeito, 6 = 1 + 2 + 3, que são seus divisores). 
    A função deve retornar um valor booleano.
"""
# Foi criado o input pq nao existe número perfeito decimal. Pelo menos na matemática básica
# Sei que poderia colocar float, pois não foi falado qual tipo de número, mas não coloquei por isso

def valorPerfeito(valor):
    
    soma = 0
    
    for div in range(1,valor):
        
        if valor % div == 0:
            soma += div
            
    if soma == valor:
        return True
    else:
        return False



while True:
    try:
        valor = int(input('Digite um valor númerico qualquer ou (0-Sai): '))

    except ValueError:
        print('Digite apenas números !!')
    
    else:
        if valor == 0:
            break

        print(f'{valor} digitado é número perfeito: {valorPerfeito(valor)}')