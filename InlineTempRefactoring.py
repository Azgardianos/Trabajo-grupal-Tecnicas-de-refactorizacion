# Refactorización de integrar una variable temporal DESPUES
class Calculadora:
    def calcular_area_rectangulo(self, ancho, alto):
        # Integrar la variable temporal 'area' directamente en la expresión de retorno
        return ancho * alto

# Uso del método refactorizado
calc = Calculadora()
area = calc.calcular_area_rectangulo(5, 3)
print(area)  # Salida: 15
