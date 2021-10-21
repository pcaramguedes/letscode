def listaNumeros(*numeros):
    soma = 0.0
    
    for i in numeros:
        soma += i
        
    return soma


print(listaNumeros(1, 23, 10.50, 14, 14.50))