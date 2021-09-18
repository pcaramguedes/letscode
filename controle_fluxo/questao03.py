#Analise o algoritmo a seguir e informe quais serão os valores de x e y ao final.

#1. x <- 3
#2. y <- 2
#3. x <- x + 1
#4. y <- x - y
#5. se y maior que 2, x <- 2

x = 3
y = 2
x += 1
y = x - y
if y > 2:
    x=2

print(x,y)
