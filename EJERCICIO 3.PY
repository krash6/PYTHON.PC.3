import math

class Circulo:

  def __init__(self, radio):
    self.radio = radio

  def calcular_area(self):
    return math.pi * self.radio ** 2


def pedir_radio():
  radio = float(input("Ingrese el radio del círculo: "))
  while radio <= 0:
    print("El radio debe ser un número positivo mayor a cero.")
    radio = float(input("Ingrese el radio del círculo: "))
  return radio


if __name__ == "__main__":
  radio = pedir_radio()
  circulo = Circulo(radio)
  area = circulo.calcular_area()
  print(f"El área del círculo es: {area}")