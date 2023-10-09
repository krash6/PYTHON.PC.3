class Rectangulo:

  def __init__(self, largo, ancho):
    self.largo = largo
    self.ancho = ancho

  def calcular_area(self):
    return self.largo * self.ancho


def pedir_dimensiones():
  largo = float(input("Ingrese el largo del rectángulo: "))
  ancho = float(input("Ingrese el ancho del rectángulo: "))
  return largo, ancho


if __name__ == "__main__":
  largo, ancho = pedir_dimensiones()
  rectangulo = Rectangulo(largo, ancho)
  area = rectangulo.calcular_area()
  print(f"El área del rectángulo es: {area}")