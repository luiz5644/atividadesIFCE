# Dado um número de três algarismos N = CDU (onde C é o algarismo das centenas, D é o algarismo das dezenas e U o algarismo das unidades), considere o número M constituído pelos algarismos de N em ordem inversa, isto é, M = UDC. Gerar M a partir de N (p.ex.: N = 123 -> M = 321).

n = int(input('Digite um numero aqui: '))

n1 = n/100
n2 = n/100
ndois =n2/10
n3 = n/1

print ('o numero {} fica {}   {}     {:.0f}'.format(n, n3, ndois, n1))
