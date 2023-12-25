# elabore um algoritmo que calcule o que deve ser pago por um produto, considerando o preço
# normal de etiqueta e a escolha da condição de pagamento. Utilize os códigos da tabela a seguir
# para ler qual a condição de pagamento escolhida e efetuar o cálculo adequado. 


v = float(input('Qual é o valor da compra:R$ '))
f = str(input('Qual é a forma de pagamento: '))


f1 = v - (v*10/100)
f2 = v - (v*10/100)
f4 = v + (v*10/100)

if f == 'dinehiro' or 'cheque':
    print('Com essa forma de pagamento você recebe 10% de desconto e o valor de {:.2f}R$, fica por {:.2f}R$'.format(v, f1))

if f == 'avista cartão':
    print('Com essa forma de pagamento você recebe 15% de desconto e seu valor de {:.2f}R$, fica por {:.2f}R$'.format(v, f2))

if f == 'parcelado em duas vezes':
    print('Com essa forma de pagamento você não recebe desconto, então o valor fica por {:.2f}R$'.format(v))

if f == 'parcelado em tres vezes':
    print('Com essa forma de pagamento rebe um acrescimo de 10%, então o valor de {:.2f}R$, fica por {:.2f}R$'.format(v, f4))



# Código Condição de pagamento 
# 1 À vista em dinheiro ou cheque, recebe 10% de desconto 
# 2 À vista no cartão de crédito, recebe 15% de desconto 
# 3 Em duas vezes, preço normal de etiqueta sem juros 
# 4 Em mais de duas vezes, preço normal de etiqueta mais juros de 10%