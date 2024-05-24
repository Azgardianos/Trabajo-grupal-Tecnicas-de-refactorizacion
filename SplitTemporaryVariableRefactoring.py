# Refactorización de dividir una variable temporal DESPUES
class Calculadora:
    def calcular(self, longitud, ancho, alto):
        area_base = longitud * ancho  # Área de la base
        volumen_prisma = area_base * alto  # Volumen del prisma
        return volumen_prisma

# Uso del método refactorizado
calc = Calculadora()
volumen = calc.calcular(2, 3, 4)
print(volumen)  # Salida:
