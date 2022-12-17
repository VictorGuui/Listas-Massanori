# Verifique se um inteiro positivo n é primo.
n = int(input('N:'))
k= 1
divisor = 0
while k <= n:                   
    if n%k==0 :
        divisor = divisor+1
    k = k+1
print (divisor == 2)


