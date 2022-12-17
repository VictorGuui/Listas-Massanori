# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo
# usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar,
# sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.
a = int(input('Quantos KM foi percorrido: '))
b = int(input('Por quantos dias foi usado: '))
kmp = a*0.15
Dia = b * 60
Tot = kmp+Dia
print('o valor a ser pago será de {}'.format(Tot)) 