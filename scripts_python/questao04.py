

try:

    n1 = float(input('Digite um número qualquer: '))

except ValueError:
    print('Campo só aceita valor numérico !!')
else:
    dobro = n1 * 2
    quadrado = n1**2
    cubo = n1**3

    print(f'O Dobro de {n1} = {dobro:.2f}')
    print(f'O Quadrado de {n1} = {quadrado:.2f}')
    print(f'O Cubo de {n1} = {cubo:.2f}')
 
