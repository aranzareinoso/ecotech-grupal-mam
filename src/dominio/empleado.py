from datetime import datetime

class Empleado:
    def __init__(self, idEmpleado: str, nombre: str, direccion: str, numero: str, direccion_de_correo: str, fecha_de_contrato: datetime, salario: float, cargo: int):
        self.idEmpleado = idEmpleado
        self.nombre = nombre
        self.direccion = direccion
        self.numero = numero
        self.direccion_de_correo = direccion_de_correo
        self.fecha_de_contrato = fecha_de_contrato
        self.salario = salario
        self.cargo = cargo

    def mostrar_datos(self) -> str:
        return f"{self.idEmpleado} - {self.nombre} - {self.numero} - {self.direccion_de_correo} - {self.fecha_de_contrato} - {self.salario} - {self.cargo} "


e = Empleado("E001", "Ana", "Calle 1", "912345678", "ana@mail.com",datetime(2026, 10, 6), 850000.0, 1)
print(e.mostrar_datos())