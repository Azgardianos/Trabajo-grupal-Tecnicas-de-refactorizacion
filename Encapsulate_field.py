class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

# Uso de la clase
persona = Persona("Juan Pérez", 30)
print(persona.nombre)
persona.edad = 31
print(persona.edad)
