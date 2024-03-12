#Gestion de consultas veterinarias

class Paciente:
    def __init__(self, nombre, identificacion, especie, sexo, motivo, telefono):
        self.__nombre= nombre
        self.__identificacion= identificacion
        self.__especie= especie
        self.__sexo= sexo
        self.motivo= motivo
        self.telefono= telefono

    def mostrarInformacion (self):
        print(f"Paciente con nombre {self.__nombre} e identificación {self.__identificacion} viene a consulta por {self.motivo}")
        



class Consulta(Paciente):
    def __init__ (self, nombre, identificacion, especie, motivo, telefono, diagnostico, tratamiento):
        super().__init__(self, nombre, identificacion, especie, motivo, telefono)
        self.diagnostico = diagnostico
        self.tratamiento = tratamiento
        self.pacientes = []

    def registrarPaciente(self, paciente):
        if paciente in self.pacientes:
            print(f"El paciente {self.__nombre} con identificacion {self.__identificacion} ya existe")
        else:
            self.pacientes.append(paciente)
            print("El paciente se agregó exitosamente")


paciente1=Paciente("max","1234","perro","macho","gripa","604321")

paciente1.mostrarInformacion()



