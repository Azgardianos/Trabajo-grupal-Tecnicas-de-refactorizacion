class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
        self._amigos = []

    # Método para añadir un amigo
    def añadir_amigo(self, amigo):
        if amigo not in self._amigos:
            self._amigos.append(amigo)

    # Método para eliminar un amigo
    def eliminar_amigo(self, amigo):
        if amigo in self._amigos:
            self._amigos.remove(amigo)

    # Método para obtener la lista de amigos
    def obtener_amigos(self):
        return list(self._amigos)  # Devolver una copia para evitar modificaciones directas

# Uso de la clase refactorizada
persona = Persona("Juan Pérez")
persona.añadir_amigo("Ana")
persona.añadir_amigo("Luis")
print(persona.obtener_amigos())
persona.eliminar_amigo("Ana")
print(persona.obtener_amigos())
