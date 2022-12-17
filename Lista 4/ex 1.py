# Sorteie 10 inteiros entre 1 e 100 para uma lista
# e descubra o maior e o menor valor, sem usar
# as funções max e min
import random

vetor = random.sample(range(0,101),10)
minimo=maximo= vetor[0]

for i in vetor[1:]:
    if i > minimo : minimo= i
    if i < maximo : maximo = i
print(minimo)
print(maximo)
print (vetor)