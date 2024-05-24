# Refactorización de integrar una variable temporal ANTES
class Calculadora:
    def calcular_area_rectangulo(self, ancho, alto):
        area = ancho * alto
        return area

# Uso del método
calc = Calculadora()
area = calc.calcular_area_rectangulo(5, 3)
print(area)  # Salida: 15
