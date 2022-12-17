# Sorteie 20 inteiros entre 1 e 100 numa lista. 
# Armazene os números pares na lista PAR e os
# números ímpares na lista IMPAR. Imprima as três listas.

import random

vetor = random.sample(range(101),20)
par = [
    x for x in vetor if x%2 == 0
]
impar=[
    x for x in vetor if x%2==1
]
print (vetor)
print(par)
print(impar)
