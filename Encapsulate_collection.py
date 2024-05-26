class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
        self.amigos = []

# Uso de la clase
persona = Persona("Juan Pérez")
persona.amigos.append("Ana")
persona.amigos.append("Luis")
print(persona.amigos)
persona.amigos.remove("Ana")
print(persona.amigos)
