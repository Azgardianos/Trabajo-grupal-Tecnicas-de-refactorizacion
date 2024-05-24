# Refactorización de introducir una variable explicativa DESPUES
class Calculadora:
    def calcular_precio_total(self, precio, impuesto, descuento):
        # Introducción de variables explicativas
        precio_con_impuesto = precio + precio * impuesto
        precio_con_descuento = precio * descuento
        precio_total = precio_con_impuesto - precio_con_descuento
        return precio_total

# Uso del método refactorizado
calc = Calculadora()
precio_total = calc.calcular_precio_total(100, 0.2, 0.1)
print(precio_total)  # Salida: 110.0
