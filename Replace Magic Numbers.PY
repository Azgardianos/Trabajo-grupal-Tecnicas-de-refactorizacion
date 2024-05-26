class Precios:
    PRODUCTO_1 = 20
    PRODUCTO_2 = 30
    IMPUESTO = 0.08

def calcular_precio_total(producto1_cantidad, producto2_cantidad):
    subtotal = (producto1_cantidad * Precios.PRODUCTO_1) + (producto2_cantidad * Precios.PRODUCTO_2)
    total = subtotal + (subtotal * Precios.IMPUESTO)
    return total

def main():
    precio_total = calcular_precio_total(3, 2)
    print(f"El precio total del pedido es: ${precio_total}")

if __name__ == "__main__":
    main()
