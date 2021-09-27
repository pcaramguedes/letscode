#### lista = []

dicio = {}.fromkeys(['nome','email'], '')

for num in range(0,2):
    
    nome = input('Entre com o seu nome: ')
    email = input('Entre com o seu e-mail: ')
    dicio = {}.fromkeys(['nome','email'], '')
    dicio['nome'] = nome
    dicio['email'] = email
    lista.append(dicio)
        
    print(num)

    
for linha in range(0,len(lista)):
    for col in dicio.keys():
    
        print(f'{lista[linha][col]}', end='\t')

        
        
    print('\n')



