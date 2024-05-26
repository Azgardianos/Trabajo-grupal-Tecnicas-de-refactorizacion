class ConversorTemperatura:
    def __init__(self, temperatura):
        self.temperatura = temperatura

class CelsiusAFahrenheit(ConversorTemperatura):
    def __init__(self, temperatura):
        super().__init__(temperatura)

    def convertir(self):
        return (self.temperatura * 9/5) + 32

class FahrenheitACelsius(ConversorTemperatura):
    def __init__(self, temperatura):
        super().__init__(temperatura)

    def convertir(self):
        return (self.temperatura - 32) * 5/9

def main():
    opcion = input("¿Qué conversión desea realizar? (Celsius a Fahrenheit [cf] o Fahrenheit a Celsius [fc]): ").lower()
    
    if opcion == "cf":
        celsius = float(input("Ingrese la temperatura en grados Celsius: "))
        convertidor = CelsiusAFahrenheit(celsius)
        resultado = convertidor.convertir()
        print(f"{celsius} grados Celsius son {resultado} grados Fahrenheit.")
    elif opcion == "fc":
        fahrenheit = float(input("Ingrese la temperatura en grados Fahrenheit: "))
        convertidor = FahrenheitACelsius(fahrenheit)
        resultado = convertidor.convertir()
        print(f"{fahrenheit} grados Fahrenheit son {resultado} grados Celsius.")
    else:
        print("Opción no válida. Por favor, ingrese 'cf' o 'fc'.")

if __name__ == "__main__":
    main()
