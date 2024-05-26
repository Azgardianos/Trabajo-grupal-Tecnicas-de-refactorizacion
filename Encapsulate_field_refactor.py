class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    # Getter para nombre
    def obtener_nombre(self):
        return self._nombre

    # Setter para nombre
    def establecer_nombre(self, nombre):
        self._nombre = nombre

    # Getter para edad
    def obtener_edad(self):
        return self._edad

    # Setter para edad
    def establecer_edad(self, edad):
        if edad >= 0:  # Validación adicional
            self._edad = edad
        else:
            raise ValueError("La edad no puede ser negativa")

# Uso de la clase refactorizada
persona = Persona("Juan Pérez", 30)
print(persona.obtener_nombre())
persona.establecer_edad(31)
print(persona.obtener_edad())
