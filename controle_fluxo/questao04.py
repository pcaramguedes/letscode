#Analise o algoritmo a seguir e informe os valores de x e y.

#1. x <- 2
#2. y <- x ** 3
#3. se y igual a 8, y <- 0
#4. caso contrário, x <- 0

x = 2
y = x ** 3

if y == 8:
    y = 0
else:
    x = 0

print(x,y)
