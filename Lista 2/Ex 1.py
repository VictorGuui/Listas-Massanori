# Faça um Programa que peça os três lados de um triângulo. O programa deverá informar se os valores podem ser
# um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
a = int(input('Digite o lado A: '))
b = int(input('Digite o lado B: '))
c = int(input('Digite o lado C: '))
if a==b==c:
    print('É um triangulo equilátero')
elif a==b or b==c or c==a:
    print('É um triangulo isóceles')
else:
    print('É um triangulo escaleno')