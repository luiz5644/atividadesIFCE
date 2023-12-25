# Um tonel de refresco é feito com 8 partes de água mineral e 2 partes de suco de maracujá. Faça um algoritmo para calcular quantos litros de água e de suco são necessários para se fazer X litros de refresco (informados pelo usuário).

qs = float(input('quantos litos de suco você quer fazer ?'))
partes = qs/100

print ('para fazer {}L de refresco, você vai precisa de {}L de água e {}L de suco'.format(qs, 80*partes, 20*partes))
