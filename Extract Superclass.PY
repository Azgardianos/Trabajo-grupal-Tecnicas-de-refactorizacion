class Empleado:
    def __init__(self, nombre):
        self.nombre = nombre

    def calcular_salario(self):
        pass

class EmpleadoPorHora(Empleado):
    def __init__(self, nombre, horas_trabajadas, tarifa_por_hora):
        super().__init__(nombre)
        self.horas_trabajadas = horas_trabajadas
        self.tarifa_por_hora = tarifa_por_hora

    def calcular_salario(self):
        return self.horas_trabajadas * self.tarifa_por_hora

class EmpleadoAsalariado(Empleado):
    def __init__(self, nombre, salario_anual):
        super().__init__(nombre)
        self.salario_anual = salario_anual

    def calcular_salario(self):
        return self.salario_anual / 12

def main():
    tipo_empleado = input("¿Qué tipo de empleado es? (Por hora [h] o Asalariado [a]): ").lower()
    nombre = input("Ingrese el nombre del empleado: ")
    
    if tipo_empleado == "h":
        horas_trabajadas = float(input("Ingrese las horas trabajadas: "))
        tarifa_por_hora = float(input("Ingrese la tarifa por hora: "))
        empleado = EmpleadoPorHora(nombre, horas_trabajadas, tarifa_por_hora)
    elif tipo_empleado == "a":
        salario_anual = float(input("Ingrese el salario anual: "))
        empleado = EmpleadoAsalariado(nombre, salario_anual)
    else:
        print("Opción no válida. Por favor, ingrese 'h' o 'a'.")
        return

    salario = empleado.calcular_salario()
    print(f"El salario del empleado ({nombre}) es: {salario}")

if __name__ == "__main__":
    main()
