class Catálogo:

  def __init__(self):
    self.productos = []

  def agregar_producto(self, producto):
    self.productos.append(producto)

  def mostrar_productos(self):
    for producto in self.productos:
      print(producto)


class Producto:

  def __init__(self, nombre, marca, modelo, año, precio):
    self.nombre = nombre
    self.marca = marca
    self.modelo = modelo
    self.año = año
    self.precio = precio


def main():
  catálogo = Catálogo()

  # Solicitar al usuario que ingrese los datos de los productos
  while True:
    nombre = input("Ingrese el nombre del producto: ")
    marca = input("Ingrese la marca del producto: ")
    modelo = input("Ingrese el modelo del producto: ")
    año = int(input("Ingrese el año del producto: "))
    precio = float(input("Ingrese el precio del producto: "))

    producto = Producto(nombre, marca, modelo, año, precio)
    catálogo.agregar_producto(producto)

    # Preguntar al usuario si desea ingresar otro producto
    opcion = input("¿Desea ingresar otro producto? (s/n): ")
    if opcion != "s":
      break

  # Filtrar los productos por año
  año_filtro = int(input("Ingrese el año a filtrar: "))
  productos_filtrados = [producto for producto in catálogo.productos if producto.año == año_filtro]

  # Mostrar los productos filtrados
  print("Productos del año {}:".format(año_filtro))
  for producto in productos_filtrados:
    print(producto)


if __name__ == "__main__":
  main()