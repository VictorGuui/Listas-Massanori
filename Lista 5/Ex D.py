# Questão D.
# Daniela é uma pessoa muito supersticiosa. Para ela, um número é sortudo
# se ele contém o dígito 2 mas não o dígito 7.
# Então, na opinião dela, quantos números
# sortudos existem entre 18644 e 33087, incluindo os extremos?
# Resposta: 7995
c = 0
for i in range (18644,33087):                       #Nesse range ele pega dentro desses valores
    if '2' in str (i) and not '7' in str (i):       #Aqui ele transforma (i) em str e pega o 2 e 7 na forma de str tbm
        c = c + 1
print(c)