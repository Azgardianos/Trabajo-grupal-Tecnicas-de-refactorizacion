class Persona:
    def __init__(self, nombre, edad, telefono, correo, direccion):
        self.nombre = nombre
        self.edad = edad
        self.telefono = telefono
        self.correo = correo
        self.direccion = direccion

    def obtener_detalles_contacto(self):
        return f"Teléfono: {self.telefono}, Correo: {self.correo}, Dirección: {self.direccion}"

    def obtener_detalles_personales(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}"

# Uso de la clase refactorizada
persona = Persona("Juan Pérez", 30, "984-345-455", "juanPe@gmail.com", "12 Av 28 de Julio")
print(persona.obtener_detalles_contacto())
print(persona.obtener_detalles_personales())
