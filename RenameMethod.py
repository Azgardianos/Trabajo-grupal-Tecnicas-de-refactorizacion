# Refactorización de renombrar método ANTES
class Calculadora:
    def suma(self, a, b):
        return a + b

# Uso del método
calc = Calculadora()
resultado = calc.suma(3, 4)
print(resultado)  # Salida: 7
