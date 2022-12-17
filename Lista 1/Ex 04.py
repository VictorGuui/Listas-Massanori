# Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a
# porcentagem do aumento. Exiba o valor do aumento e do novo salário.

a = int(input('Digite o seu salário:'))
b = int(input('Qual a porcentagem que sera adicionada ao salário?'))
soma = (a*b)/100

print('Seu novo salario {} e o adicional foi de {}'.format(soma+a,soma))