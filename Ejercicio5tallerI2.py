#creamos clase tarea

class Tarea:
    def __init__(self, descripcion, prioridad, completada):
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.completada = completada

    def tareaCompletada(self):
        self.completada = True

    def editarDescripcion(self, descripcion_n): #corregir esto porque no se
        self.descripcion = descripcion_n

    def editarPrioridad(self, prioridad_n): #corregir esto porque no se
        self.prioridad = prioridad_n

    def mostrarInformacion(self):
        print(f"La tarea {self.descripcion} tiene prioridad {self.prioridad} y se encuentra {self.completada}.")


class listaTareas:
    def __init__(self):
        self.tareas = []

    def agregarTarea(self,tarea):
        self.tareas.append(tarea)
        
    def verPendientes(self,tarea):
        if tarea in self.tareas:
            print(f"La tarea {tarea.descripcion} esta pendiente")
        
        else:
            print("La tarea fue completada")


tarea1=Tarea("Matematicas","Alta", "completada")

tarea1.mostrarInformacion()

