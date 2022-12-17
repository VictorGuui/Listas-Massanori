#!/usr/bin/python -tt
# Exercícios by Nick Parlante (CodingBat)

# B. lone_sum
# Soma maluca: some os números inteiros a, b, e c
# Se algum número aparecer repetido ele não conta na soma
# lone_sum(1, 2, 3) -> 6
# lone_sum(3, 2, 3) -> 2
# lone_sum(3, 3, 3) -> 0
def lone_sum(a, b, c):
  return

# C. luck_sum #
# Soma três inteiros a, b, c
# Se aparecer um 13 ele não conta e todos os da sua direita também
# lucky_sum(1, 2, 3) -> 6
# lucky_sum(1, 2, 13) -> 3
# lucky_sum(1, 13, 3) -> 1
def lucky_sum(a, b, c):
  return
# I. count_evens
# conta os números pares da lista
# count_evens([2, 1, 2, 3, 4]) -> 3           Tirar duvidas cm o pessoa
# count_evens([2, 2, 0]) -> 3
# count_evens([1, 3, 5]) -> 0
def count_evens(nums):
  return
# K. has22 #
# Verifica se na lista de números inteiros aparecem dois 2 consecutivos
# has22([1, 2, 2]) -> True
# has22([1, 2, 1, 2]) -> False
# has22([2, 1, 2]) -> False
def has22(nums):
  return 

# Provided simple test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(obtido, esperado):
  if obtido == esperado:
    prefixo = ' Parabéns!'
  else:
    prefixo = ' Ainda não'
  print ('%s obtido: %s esperado: %s'
         % (prefixo, repr(obtido), repr(esperado)))

def main():

  print ()
  print ('Lone Sum')
  test(lone_sum(1, 2, 3), 6)
  test(lone_sum(3, 2, 3), 2)
  test(lone_sum(3, 3, 3), 0)
  test(lone_sum(9, 2, 2), 9)
  test(lone_sum(2, 2, 9), 9)
  test(lone_sum(2, 9, 2), 9)
  test(lone_sum(2, 9, 3), 14)
  test(lone_sum(4, 2, 3), 9)
  test(lone_sum(1, 3, 1), 3)

  print ()
  print ('Lucky_sum')
  test(lucky_sum(1, 2, 3), 6)
  test(lucky_sum(1, 2, 13), 3)
  test(lucky_sum(1, 13, 3), 1)
  test(lucky_sum(1, 13, 13), 1)
  test(lucky_sum(6, 5, 2), 13)
  test(lucky_sum(13, 2, 3), 0)
  test(lucky_sum(13, 2, 13), 0)
  test(lucky_sum(13, 13, 2), 0)
  test(lucky_sum(9, 4, 13), 13)
  test(lucky_sum(8, 13, 2), 8)
  test(lucky_sum(7, 2, 1), 10)
  test(lucky_sum(3, 3, 13), 6)

  print ()
  print ('Count_evens')
  test(count_evens([2, 1, 2, 3, 4]), 3)
  test(count_evens([2, 2, 0]), 3)
  test(count_evens([1, 3, 5]), 0)
  test(count_evens([]), 0)
  test(count_evens([11, 9, 0, 1]), 1)
  test(count_evens([2, 11, 9, 0]), 2)
  test(count_evens([2]), 1)
  test(count_evens([2, 5, 12]), 2)

  print ()
  print ('Has22')
  test(has22([1, 2, 2]), True)
  test(has22([1, 2, 1, 2]), False)
  test(has22([2, 1, 2]), False)
  test(has22([2, 2, 1, 2]), True)
  test(has22([1, 3, 2]), False)
  test(has22([1, 3, 2, 2]), True)
  test(has22([2, 3, 2, 2]), True)
  test(has22([4, 2, 4, 2, 2, 5]), True)
  test(has22([1, 2]), False)
  test(has22([2, 2]), True)
  test(has22([2]), False)
  test(has22([]), False)
  test(has22([3, 3, 2, 2]), True)
  test(has22([5, 2, 5, 2]), False)

if __name__ == '__main__':
  main()