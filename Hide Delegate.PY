class Departamento:
    def __init__(self, nombre):
        self.nombre = nombre

class Empleado:
    def __init__(self, nombre, departamento):
        self.nombre = nombre
        self._departamento = departamento

    def obtener_nombre_departamento(self):
        return self._departamento.nombre

def main():
    departamento = Departamento("Finanzas")
    empleado = Empleado("Juan", departamento)
    print(f"El empleado {empleado.nombre} trabaja en el departamento de {empleado.obtener_nombre_departamento()}")

if __name__ == "__main__":
    main()
