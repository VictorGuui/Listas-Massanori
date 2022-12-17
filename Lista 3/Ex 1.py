# Dizemos que um número natural é triangular se ele é produto de três números naturais consecutivos. Exemplo: 120 é triangular, pois 4.5.6 = 120. 
# Dado um inteiro não-negativo n,verificar se n é triangular.

n= int(input('N: '))            
k = 0
while k * (k+1)*(k+2)<n:        #Enquanto k for menor que n ele faz o loop até chegar no valor de n
    k = k +1                    #após chegar no valor de n ele soma +1 e +2 
print(k * (k+1)*(k+2)==n)       #ao chegar aqui ele pega o 1ºk e multiplica pelo 'k2' e 'k3'