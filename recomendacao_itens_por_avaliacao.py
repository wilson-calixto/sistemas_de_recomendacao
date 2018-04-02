from base_de_dados_invertida import avaliacoes, topicos
from math import sqrt
import numpy as np

def euclidiana (usuario1, usuario2):
    i = False
    for item in avaliacoes[usuario1]:
        if item in avaliacoes[usuario2]:
            i = True
            break
    if not i:
        return 0
    r = sqrt(sum([pow(avaliacoes[usuario1][item] - avaliacoes[usuario2][item], 2) for item in avaliacoes[usuario1] if item in avaliacoes[usuario2]]))
    return (1/(1+r))
    #c = sqrt(sum((avaliacoes[usuario1].get(d, 0) - avaliacoes[usuario2].get(d, 0)) ** 2 for d in set(avaliacoes[usuario1]) & set(avaliacoes[usuario2])))
    #print (1/(1+c))

def getSimilares(usuario):
    similaridade = [(euclidiana(usuario, outro), outro) for outro in avaliacoes if outro != usuario]
    similaridade.sort()
    similaridade.reverse()
    return similaridade

def getRecomendacoes(usuario):
    totais = {}
    somaSimilaridade = {}
    for outro in avaliacoes:
        if outro == usuario: continue
        similaridade = euclidiana(usuario, outro)
        if similaridade <= 0: continue
        for item in avaliacoes[outro]:
            #### somente o que o usuário alvo ainda não avaliou
            if item not in avaliacoes[usuario]:
                totais.setdefault(item, 0)
                totais[item] += avaliacoes[outro][item] * similaridade
                somaSimilaridade.setdefault(item, 0)
                somaSimilaridade[item] += similaridade
    rankings = [(total/somaSimilaridade[item], item) for item, total in totais.items()]
    rankings.sort()
    rankings.reverse()
    return rankings
print("Numero:         topico")
for i in range(len(topicos)):
	if(i % 2 ==0):
		print("   ",i,"---------",topicos[i])
	else:
		print("   ",i,"         ",topicos[i])

topico_escolhido=int(input("Digite o numero do topico que vocẽ deseja\n"))


if (topico_escolhido >=0 and topico_escolhido < len(topicos)):
	print(getSimilares(topicos[topico_escolhido]))
else:
	print("Vocẽ digitou um numero inválido")
