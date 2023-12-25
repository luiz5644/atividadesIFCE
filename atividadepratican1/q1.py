gasolina = float(input("Qual é o valor da gasolina: R$ "))
etanol = float(input("Qual é o valor do etanol: R$"))

valor_etanol70 = etanol + (0.7*etanol)

if valor_etanol70 > gasolina:
    print("o recomendado é você abastecer com gasolina")
else:
    print("o recomendado é você abastecer com etanol")