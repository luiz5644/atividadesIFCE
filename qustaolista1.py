# aqui ele vai pedir palavras e essa palavras vão ser adicionadas em um lista 

lista = [] #lista vazia

for i in range (6):#leitura de 6 palavras
    p = input('palavra: ')
    lista.append(p)

lista.sort() #ordenação crescente
print (lista)

