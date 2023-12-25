# Leia 4 valores inteiros A, B, C e D. A seguir, se B for maior do que C e se D for maior do que A, e a soma de C com D for maior que a soma de A e B e se C e D
, ambos, forem positivos e se a variável A for par escrever a mensagem , senão escrever .


A = int(input('digite um valor para A: '))
B = int(input('digite um valor para B: '))
C= int(input('digite um valor para C: '))
D = int(input('digite um valor para D: '))

somacd = C + D
somaab = A + B

if B > C and D > A and somacd > somaab and c > 0 and d > 0:
    print('sim')
else: 
    print('não')
