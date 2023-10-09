class Calificaciones:

  def __init__(self, calificaciones):
    self.calificaciones = calificaciones

  def convertir_calificaciones(self):
    calificaciones_convertidas = []
    for calificacion in self.calificaciones:
      try:
        calificaciones_convertidas.append(int(calificacion))
      except ValueError:
        print(f"La calificación '{calificacion}' no es válida")
    return calificaciones_convertidas


def main():
  calificaciones = input("Ingrese una lista de calificaciones separadas por comas: ")
  calificaciones_objeto = Calificaciones(calificaciones)
  calificaciones_convertidas = calificaciones_objeto.convertir_calificaciones()
  print(f"Las calificaciones convertidas son: {calificaciones_convertidas}")


if __name__ == "__main__":
  main()