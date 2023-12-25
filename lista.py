# assunto: lista

# - é uma coleção(conjunto) de dados do mesmo tipo, ou não 
# - é representada por única variável

# 2. Declaração de uma lista 
# lista = []
# índice: 0 1 2
# lista = [10, 20, 30]

# lista de um número até  outro 
# lista = [0]*100

# valores de 1 a 50 
# lista = list(range(1, 51))
# print (lista)

# 3. apresentação em tela 
# a - forma direta
# print(lista)

# b - forma seletiva - um em baixo do outro 
# for i in lista:
#     print(i)

# um do lado do outro sem ,
# for i in lista:
#     print(i, end = ' ')

# apenas um número 
# print (lista[2])

# uma fatia 
# print (lista[9:20])

# 4 funções 
# a calcular tamanho 
# from ast import Index


# lista=['casa', 'hotel', 'escolas', 'mercado']
# t = len(lista)
# print ("Tamanho da lista: {}".format(t))

# b - contagem de ocorrência
# cont = lista.count('casa')
# print ('n de vezes que aparece a palavra casa {}'.format(cont))

# c ordenaçao da lista
# lista.sort() #acrescente
# print (lista)

# lista.sort(reverse=True) #decrescente
# print(lista)

# d inversão da ordem dos valore em uma lista
# inums =[2, 5, 1, 0, 3]
# inums.reverse()
# print(inums)

# e checagem de elementos em uma lista
# lista = ['Casa', 'Hotel', 'Escola', 'Mercado']
# exista = 'Hotel' in lista
# print(exista)

# if 'Casa' in lista:
#     print('Sim')

# else:
#     print ('Não')


# # f identificar o índice de um Valor 
# if 'escolas' in lista:
#     pos = lista.index('escolas')
#     print ('indeice: {}'.format(pos+1))
# else:
#     print('Termo não encontrado')

# comandos de manipulação da lista
# 1 adicionar elementos
# lista = []
# lista.append('pedro')
# lista.append('ana')
# lista.append('caio')
# print('lista {}'.format(lista))

# print ('digite um valor aqui')
# nome = input()
# lista.append(nome)
#     # nome = input()
#     # lista.append(nome)
# print(lista)


# 2 adicinar elementos em um indice específico 
# lista = [10, 30]
# lista.insert(_index:10, _object:20 )
# print (lista)

# 3 remover um item em especifico

# lista.remove(1)
# print ('lista')

# 4 apagar todos os elementos da lista
# lista.clear()
# lista =[]

# 5 junção de listas 
# l1 = [1, 2, 3]
# l2 = [4, 5, 5]
# ls = l1 + l2 f1
# print (ls)

# l1.extend(l2)
# print (l1)

# exclusao de item pelo indice 

# del(l1[4])
# print(l1)

# exclusão do ultimo elemento 
# del (l1[-1])
# l1.popL(4)
# print(l1)

# 7 criar cópia de uma lista
# l1 = [1, 2, 3]
# copia = l1
# copia.pop()
# print(l1)