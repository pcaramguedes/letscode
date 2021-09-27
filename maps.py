"""
 Mapas em python são dicionários
 Dicionários em python são representados por {}
 print(receita)
# Acessando chaves
for chave in receita.keys():
    print(receita[chave])

# Acessando valores
print(receita.values())

for valor in receita.values():
    print(valor)
    
    
#desempacotamento de dicionarios

print(receita.items())

for chave, valor in receita.items():
    print(f'{chave} e {valor}')

"""

receita = {'jan':1500,'fev':2000,'mar':2300.00}

# Acessando valores
print(receita.values())

for valor in receita.values():
    print(valor)
    
    
#desempacotamento de dicionarios

print(receita.items())

for chave, valor in receita.items():
    print(f'{chave} e {valor}')
