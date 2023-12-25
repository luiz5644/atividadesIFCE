import random
palavras = [
    ('casa', 'Dica: construção'),
    ('bola', 'Dica: objeto'),
    ('mangueira', 'Dica: planta'),
    ('uva', 'Dica: fruta'),
    ('quiabo', 'Dica: alimento'),
    ('computador', 'Dica: objeto'),
    ('café', 'Dica: bebida'),
    ('refrigerante', 'Dica: bebida'),
    ('mouse', 'Dica: objeto'),
    ('teclado', 'Dica: objeto'),
    ('calendário', 'Dica: objeto'),
    ('carro', 'Dica: veículo'),
    ('tesoura', 'Dica: objeto'),
    ('carteira', 'Dica: objeto'),
    ('caneta', 'Dica: objeto'),
    ('livro', 'Dica: objeto'),
    ('jornal', 'Dica: objeto'),
]
palavraRandom, dicaPalavra = random.choice(palavras)
palavraRandomLetras = len(palavraRandom)
base = ['_'] * palavraRandomLetras
tentativasMax = 6
erros = 0
#print(palavraRandom) #debug
while tentativasMax > 0:
    print('         Jogo da Forca')
    print('       Descubra a palavra: \n          ')
    match erros:
            case 0:
                print('  _______')
                print(' |/      |'  )
                print(' |      (_) ')
                print(' |        '  )
                print(' |'          )
                print(' |'          )
                print(' |',''.join(base))
                print('')
            case 1:
                print('  _______'   )
                print(' |/      |'  )
                print(' |      (_)' )
                print(' |       |'  )
                print(' |'          )
                print(' |'          )
                print(' |',''.join(base))
                print('')
            case 2:
                print('  _______')
                print(' |/      |'  )
                print(' |      (_)' )
                print(' |      /| ')
                print(' |'          )
                print(' |'          )
                print(' |',''.join(base))
                print('')
            case 3:
                print('  _______')
                print(' |/      |'  )
                print(' |      (_)' )
                print(' |      /|\ ')
                print(' |       |'  )
                print(' |'          )
                print(' |',''.join(base))
                print(f'{dicaPalavra}')
            case 4:
                print('  _______'   )
                print(' |/      |'  )
                print(' |      (_)' )
                print(' |      /|\ ' )
                print(' |       |'  )
                print(' |       \ ' )
                print(' |',''.join(base))
                print(f'{dicaPalavra}')
            case 5:
                print('  _______'   )
                print(' |/      |'  )
                print(' |      (_)' )
                print(' |      /|\ ' )
                print(' |       |'  )
                print(' |       \_' )
                print(' |',''.join(base))
                print(f'{dicaPalavra}')
            case 6:
                print('  _______')
                print(' |/      |  ')
                print(' |      (_) ')
                print(' |      /|\ ')
                print(' |       |  ')
                print(' |      _/\_')
                print(' |',''.join(base))
                print('Você perdeu!')
    resposta = str(input('Digite uma letra: ')).lower()
    if resposta in palavraRandom:
        print('A letra digitada está na palavra')
        print('  _______'   )
        print(' |/      |'  )
        print(' |      (_)' )
        print(' |      /|\ ' )
        print(' |       |'  )
        print(' |     _/\_' )
        print(' |',''.join(base))
        for c in range(palavraRandomLetras):
            if resposta == palavraRandom[c]:
                base[c] = resposta
    else:
        print('A letra digitada não está na palavra')
        print('A palavra é: ', ''.join(base))
        tentativasMax -= 1
        erros += 1
        

    if ''.join(base) == palavraRandom:
        print('A palavra é: ', ''.join(base))
        print('Você ganhou!')
        break