#!/usr/bin/python -tt
# Exercícios by Nick Parlante (CodingBat)

# B. string_splosion
# string_splosion('Code') -> 'CCoCodCode'
# string_splosion('abc') -> 'aababc'
# string_splosion('ab') -> 'aab'
def string_splosion(s):
  return

# D. array_front9
# verifica se pelo menos um dos quatro primeiros é nove
# array_front9([1, 2, 9, 3, 4]) -> True
# array_front9([1, 2, 3, 4, 9]) -> False
# array_front9([1, 2, 3, 4, 5]) -> False
def array_front9(nums):
  return

# I. sem_pontas
# seja uma string s de pelo menos dois caracteres
# retorna uma string sem o primeiro e último caracter
# without_end('Hello') -> 'ell'
# without_end('python') -> 'ytho'
# without_end('coding') -> 'odin'
def sem_pontas(s):
  return   

# J. roda2
# rodar uma string s duas posições
# a string possui pelo menos 2 caracteres
# left2('Hello') -> 'lloHe'
# left2('Hi') -> 'Hi'
def roda2(s):
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
  print ('String Explosion')
  test(string_splosion('Code'), 'CCoCodCode')
  test(string_splosion('abc'), 'aababc')
  test(string_splosion('ab'), 'aab')
  test(string_splosion('x'), 'x')
  test(string_splosion('fade'), 'ffafadfade')
  test(string_splosion('There'), 'TThTheTherThere')
  test(string_splosion('Kitten'), 'KKiKitKittKitteKitten')
  test(string_splosion('Bye'), 'BByBye')
  test(string_splosion('Good'), 'GGoGooGood')
  test(string_splosion('Bad'), 'BBaBad')
  
  print ()
  print ('Array front 9')
  test(array_front9([1, 2, 9, 3, 4]), True)
  test(array_front9([1, 2, 3, 4, 9]), False)
  test(array_front9([1, 2, 3, 4, 5]), False)
  test(array_front9([9, 2, 3]), True)
  test(array_front9([1, 9, 9]), True)
  test(array_front9([1, 2, 3]), False)
  test(array_front9([1, 9]), True)
  test(array_front9([5, 5]), False)
  test(array_front9([2]), False)
  test(array_front9([9]), True)
  test(array_front9([]), False)
  test(array_front9([3, 9, 2, 3, 3]), True)

  print ()
  print ('Sem Pontas')
  test(sem_pontas('Hello'), 'ell')
  test(sem_pontas('Python'), 'ytho')
  test(sem_pontas('coding'), 'odin')
  test(sem_pontas('code'), 'od')
  test(sem_pontas('ab'), '')
  test(sem_pontas('Chocolate!'), 'hocolate')
  test(sem_pontas('kitten'), 'itte')
  test(sem_pontas('woohoo'), 'ooho')

  print ()
  print ('Roda 2')
  test(roda2('Hello'), 'lloHe')
  test(roda2('python'), 'thonpy')
  test(roda2('Hi'), 'Hi')
  test(roda2('code'), 'deco')
  test(roda2('cat'), 'tca')
  test(roda2('12345'), '34512')
  test(roda2('Chocolate'), 'ocolateCh')
  test(roda2('bricks'), 'icksbr')

if __name__ == '__main__':
  main()