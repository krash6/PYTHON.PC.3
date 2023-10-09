import random


def generar_numeros_aleatorios():
  """
  Genera 20 números enteros aleatorios entre 0 y 100 y devuelve una lista.

  Returns:
    Una lista con 20 números enteros aleatorios entre 0 y 100.
  """

  lista = []
  for i in range(20):
    numero = random.randint(0, 100)
    lista.append(numero)
  return lista


def mostrar_lista(lista):
  """
  Muestra la lista obtenida por pantalla.

  Args:
    lista: La lista que se desea mostrar.
  """

  print("Lista original:")
  for numero in lista:
    print(numero)


def ordenar_lista(lista):
  """
  Ordena los valores de la lista y muestra la lista por pantalla.

  Args:
    lista: La lista que se desea ordenar.
  """

  lista.sort()
  print("Lista ordenada:")
  for numero in lista:
    print(numero)


if __name__ == "__main__":
  lista = generar_numeros_aleatorios()
  mostrar_lista(lista)
  ordenar_lista(lista)