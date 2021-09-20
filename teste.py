produto = []

soma = 0.0
contador = 0
while True:
    valor = float(input('Valor do Produto ou (0-Sai): '))
    
    if valor == 0.00:
        break
    
    produto.append(valor)
    soma += produto[contador]
    contador += 1


if valor == 0.0 and len(produto) > 0:
    
    num = 0
    
    while num < len(produto):
        print(produto[num])
        num += 1

    print(f'Total da compra: R$ {soma:.2f}')
    dinheiro = float(input('Recebimento - Dinheiro: '))
    troco = soma - dinheiro
    print(f'Troco: R$ {troco:.2f}')
    
