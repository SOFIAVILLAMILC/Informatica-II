#biblioteca
from datetime import datetime, timedelta

class Item:
    def __init__(self, titulo):
        self.titulo = titulo
        self.disponible = True
        self.fechaPrestamo = None
        self.fechaRetorno = None

    def prestar(self, tipoPrestamo):
        self.disponible = False
        self.fechaPrestamo = datetime.now()
        if tipoPrestamo == "Corto":
            self.fechaRetorno = self.fechaPrestamo + timedelta(weeks=1)
        elif tipoPrestamo == "Largo":
            self.fechaRetorno = self.fechaPrestamo + timedelta(weeks=3)

    def devolver(self):
        self.disponible = True
        self.fechaPrestamo = None
        self.fechaRetorno = None

class Libro(Item):
    def __init__(self, titulo, tipoPrestamo):
        super().__init__(titulo)
        self.tipoPrestamo = tipoPrestamo

class Revista(Item):
    def __init__(self, titulo):
        super().__init__(titulo)

class Miembro:
    def __init__(self, nombre, staff=False):
        self.nombre = nombre
        self.staff = staff

class Biblioteca:
    def __init__(self):
        self.catalogo = []

    def agregarItem(self, item):
        self.catalogo.append(item)

    def prestarItem(self, titulo, tipoPrestamo, miembro):
        for item in self.catalogo:
            if item.titulo == titulo and item.disponible:
                if isinstance(item, Revista):
                    if miembro.staff:
                        item.prestar(tipoPrestamo)
                        return True
                    else:
                        return False  # No se permite prestar revistas a no ser que sea miembro del staff
                else:
                    item.prestar(tipoPrestamo)
                    return True
        return False  # No se encontró el item o no está disponible

    def devolverItem(self, titulo):
        for item in self.catalogo:
            if item.titulo == titulo:
                item.devolver()
                return True
        return False  # No se encontró el item


biblioteca = Biblioteca()

libro1 = Libro("El Señor de los Anillos", "Largo")
libro2 = Libro("Cien años de soledad", "Corto")
revista1 = Revista("National Geographic")

biblioteca.agregarItem(libro1)
biblioteca.agregarItem(libro2)
biblioteca.agregarItem(revista1)

miembro = Miembro("Juan")
staff = Miembro("Ana", staff=True)

# Préstamo de libros
print(biblioteca.prestarItem("El Señor de los Anillos", "Largo", miembro))
print(biblioteca.prestarItem("Cien años de soledad", "Corto", miembro))

# Préstamo de revistas (solo para miembros del staff)
print(biblioteca.prestarItem("National Geographic", "Corto", staff))
print(biblioteca.prestarItem("National Geographic", "Corto", staff))

# Devolución de libros

print(biblioteca.devolverItem("El Señor de los Anillos"))
print(biblioteca.devolverItem("Cien años de soledad"))