#15. (Desafio) Imagine que você está desenvolvendo o programa de um caixa eletrônico para que os usuários realizem saques em dinheiro. Leia um valor inteiro, a seguir calcule o menor número de notas possíveis (cédulas) no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5 e 2.

from time import sleep

nota = int(input('Digite aqui um valor a ser trocado:R$'))
print('Calculando....')
sleep (2)

resto1 = nota  // 100
n1 = nota - (resto1 * 100)

resto2 = n1 // 50
n2 = n1 - (resto2 *50)

resto3 = n2 // 20
n3 = n2 - (resto3 * 20)

resto4 = n3 // 10
n4 = n3 - (resto4 * 10)

resto5 = n4 // 5
n5 = n4 - (resto5 * 5)

resto6 = n5 // 2
n6 = n5 - (resto6 *2)

if resto1 > 0 or resto2 > 0 or resto3 > 0 or resto4 > 0 or resto5 > 0 or resto6 > 0:
    print ('você vai precisar de {} nota(s) de 100R$\nvocê vai precisar de {} nota(s) de 50R$\nvocê vai precisar de {} nota(s) de 20R$\nvocê vai precisar de {} nota(s) de 10R$\nvocê vai precisar de {} nota(s) de 5R$\nvocê vai precisar de {} nota(s) de 2R$'.format(resto1, resto2, resto3, resto4, resto5, resto6 ))
