# Refactorización de renombrar método DESPUES
class Calculadora:
    def agregar(self, a, b):
        return a + b

# Uso del método refactorizado
calc = Calculadora()
resultado = calc.agregar(3, 4)
print(resultado)  # Salida: 7
