# Refactorización de introducir una variable explicativa ANTES
class Calculadora:
    def calcular_precio_total(self, precio, impuesto, descuento):
        return precio + precio * impuesto - precio * descuento

# Uso del método
calc = Calculadora()
precio_total = calc.calcular_precio_total(100, 0.2, 0.1)
print(precio_total)  # Salida: 110.0
