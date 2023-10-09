class Alumno:

  def __init__(self):
    self.nombre = None
    self.numero_registro = None
    self.edad = None
    self.notas = []

  def mostrar(self):
    print(f"Nombre: {self.nombre}")
    print(f"Número de registro: {self.numero_registro}")
    if self.edad is not None:
      print(f"Edad: {self.edad}")
    if self.notas:
      print(f"Notas: {self.notas}")

  def set_nombre(self, nombre):
    self.nombre = nombre

  def set_numero_registro(self, numero_registro):
    self.numero_registro = numero_registro

  def set_edad(self, edad):
    self.edad = edad

  def set_notas(self, notas):
    self.notas = notas


def pedir_datos():
  nombre = input("Ingrese el nombre del estudiante: ")
  numero_registro = input("Ingrese el número de registro del estudiante: ")
  edad = input("Ingrese la edad del estudiante: ")
  notas = []
  for nota in input("Ingrese las notas del estudiante, separadas por espacios: ").split():
    nota = float(nota)
    notas.append(nota)
  return nombre, numero_registro, edad, notas


if __name__ == "__main__":
  alumno = Alumno()
  nombre, numero_registro, edad, notas = pedir_datos()
  alumno.set_nombre(nombre)
  alumno.set_numero_registro(numero_registro)
  alumno.set_edad(edad)
  alumno.set_notas(notas)
  alumno.mostrar()