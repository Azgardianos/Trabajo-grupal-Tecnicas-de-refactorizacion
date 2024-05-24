# Refactorización de dividir una variable temporal ANTES
class Calculadora:
    def calcular(self, longitud, ancho, alto):
        temp = longitud * ancho  # Área de la base
        temp = temp * alto       # Volumen del prisma
        return temp

# Uso del método
calc = Calculadora()
volumen = calc.calcular(2, 3, 4)
print(volumen)  # Salida: 24
