#Sabendo que A <- 3, B <- 5, C <- 6. Responda Verdadeiro ou Falso.

#    A maior que B? = Falso
#    (A+C) maior que C? = Verdadeiro
#    (A * 2) igual a C? = Verdadeiro 
#    C - B igual a 1? = Verdadeiro
#    (A - B) igual a (B - C + 1)? = False

a = 3
b = 5
c = 6

if a > 6:
    print('Verdadeiro')
else:
    print('Falso')

if (a+c) > c:
    print('Verdadeiro')
else:
    print('Falso')

if (a*2) == c:
    print('Verdadeiro')
else:
    print('Falso')

if (c -b) == 1:
    print('Verdadeiro')
else:
    print('Falso')

if (a-b) == (b-c+1):
    print('Verdadeiro')
else:
    print('falso')

