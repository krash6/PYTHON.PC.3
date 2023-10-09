class Punto:

  def __init__(self, x=0, y=0):
    self.x = x
    self.y = y

  def __str__(self):
    return f"({self.x}, {self.y})"

  def cuadrante(self):
    if self.x == 0 and self.y != 0:
      return 1
    elif self.x != 0 and self.y == 0:
      return 2
    elif self.x > 0 and self.y > 0:
      return 1
    elif self.x < 0 and self.y > 0:
      return 2
    elif self.x < 0 and self.y < 0:
      return 3
    elif self.x > 0 and self.y < 0:
      return 4
    else:
      return 0

  def vector(self, punto):
    return Punto(self.x - punto.x, self.y - punto.y)

  def distancia(self, punto):
    return math.sqrt((self.x - punto.x)**2 + (self.y - punto.y)**2)


def main():
  # Solicitar al usuario que ingrese las coordenadas del punto
  x = float(input("Ingrese la coordenada X del punto: "))
  y = float(input("Ingrese la coordenada Y del punto: "))

  # Crear un punto con las coordenadas ingresadas por el usuario
  punto = Punto(x, y)

  # Imprimir el punto
  print(punto)

  # Imprimir el cuadrante del punto
  print(punto.cuadrante())

  # Solicitar al usuario que ingrese las coordenadas del otro punto
  x2 = float(input("Ingrese la coordenada X del otro punto: "))
  y2 = float(input("Ingrese la coordenada Y del otro punto: "))

  # Crear el otro punto con las coordenadas ingresadas por el usuario
  punto2 = Punto(x2, y2)

  # Imprimir el vector resultante entre los dos puntos
  vector = punto.vector(punto2)
  print(vector)

  # Imprimir la distancia entre los dos puntos
  distancia = punto.distancia(punto2)
  print(distancia)


if __name__ == "__main__":
  main()