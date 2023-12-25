n = 1
soma = 0
while n != 0:
    n = int(input('digite um número com dois dígitos aqui: '))
    if n >= 10 and n <=99:
        soma += n
    elif n == 0:
        break
    else:
        pass
print('a soma de todos os numeros é igual a {}'.format(soma))
    