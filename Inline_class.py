class InformacionContacto:
    def __init__(self, telefono, correo, direccion):
        self.telefono = telefono
        self.correo = correo
        self.direccion = direccion

    def obtener_detalles(self):
        return f"Teléfono: {self.telefono}, Correo: {self.correo}, Dirección: {self.direccion}"

class Persona:
    def __init__(self, nombre, edad, informacion_contacto):
        self.nombre = nombre
        self.edad = edad
        self.informacion_contacto = informacion_contacto

    def obtener_detalles_contacto(self):
        return self.informacion_contacto.obtener_detalles()

    def obtener_detalles_personales(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}"

# Uso de las clases
informacion_contacto = InformacionContacto("984-345-455", "juanPe@gmail.com", "12 Av 28 de Julio")
persona = Persona("Juan Pérez", 30, informacion_contacto)
print(persona.obtener_detalles_contacto())
print(persona.obtener_detalles_personales())
