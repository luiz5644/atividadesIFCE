# Bem, eu fiz essa urna com oque eu aprendi e sei (até agora), então ela é bem simpres, ela me mostra o total de voto dos candidatos, os candidatos e os seus números e caso o eleitor digite um número errado, esse número vai para contagem de votos nulos. é isso.



votos_silverio_reais = 0
votos_monteiro_lobato = 0
votos_elis_regina = 0
votos_nulos = 0


while True:
    print("-" * 25)
    print("     TOTAL DE VOTOS     \nSILVÉRIO REAIS(PTC): {}\nMONTEIRO LOBATO(PT): {}\nELIS REGINA(PDT)   : {}\nVOTOS NULOS        : {}".format(votos_silverio_reais, votos_monteiro_lobato, votos_elis_regina, votos_nulos))
    print("-" * 25)

    voto = int(input("      URNA TABUALGO      \n45 - SILVÉRIO REAIS  (PTC)\n13 - MONTEIRO LOBATO (PT)\n12 - ELIS REGINA     (PDT)\nPara quem é o seu voto ? "))
    

    if voto ==45:
        votos_silverio_reais +=1
    elif voto == 13:
        votos_monteiro_lobato +=1
    elif voto ==12:
        votos_elis_regina +=1
    else:
        votos_nulos += 1
   
    