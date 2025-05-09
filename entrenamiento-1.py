print("--- SISTEMA DE COMPRAS SIMPLE ---")

    # Pedir documento con validacion de error
while True:
    try:
        documento = float(input("Ingrese su documento (solo números): "))
        break  # Si llega aquí, el número es válido, sigue con el codigo 
    except:
        print("¡Error! El documento debe contener solo números. Intente nuevamente.") # esto le va salir si ingresa un valor diferente

# Pedir nombre no necesita validación compleja

nombre = input("Ingrese su nombre: ").upper()

#PRODUCTO
# Pedir producto validación básica
while True:
    producto = input("Ingrese el producto: ").upper()
    if producto.strip() != "":  # Verifica que no esté vacío
        break
    else:
        print("¡Error! Debe ingresar un nombre de producto.")

#VALOR DEL PRODUCTO
# Pedir valor del producto con validación
while True:
    try:
        valor = float(input("Ingrese el valor del producto: $"))
        if valor > 0:  # El valor debe ser positivo
            break
        else:
            print("¡Error! El valor debe ser mayor a cero.")
    except:
        print("¡Error! Debe ingresar un número válido.")

#CANTIDAD QUE VA A LLEVAR
# Pedir cantidad con validación
while True:
    try:
        cantidad = float(input("Ingrese la cantidad que lleva: "))
        if cantidad > 0:  # La cantidad debe ser positiva
            break
        else:
            print("¡Error! La cantidad debe ser mayor a cero.")
    except:
        print("¡Error! Debe ingresar un número válido.")

# Calcular total sin descuento
total_sin_descuento = valor * cantidad

# Preguntar por descuento
while True:
    try:
        print("\n¿Desea aplicar un descuento?")
        opcion = int(input("1. Sí\n2. No\nElija un numero entre (1 o 2): "))

        if opcion == 1 or opcion == 2:
            break  # Opción válida
        else:
            print("¡Error! Opción no válida. Debe ser 1 o 2.")
    except:
        print("¡Error! Debe ingresar 1 o 2.")

# Manejar descuento si eligió la opción 1
if opcion == 1:
    while True:
        try:
            descuento = int(input("Ingrese el porcentaje de descuento (1-100%): "))
            if 1 <= descuento <= 100:  # Descuento entre 1% y 100%
                monto_descuento = total_sin_descuento * (descuento / 100)
                total_con_descuento = total_sin_descuento - monto_descuento
                break
            else:
                print("¡Error! El descuento debe estar entre 1% y 100%.")
        except:
            print("¡Error! Debe ingresar un número válido.")
else:
    monto_descuento = 0
    total_con_descuento = total_sin_descuento

    # Mostrar resumen de la compra
print("\n--- RESUMEN DE COMPRA ---")
print(f"Cliente: {nombre} (Documento: {documento:.0f})")
print(f"Producto: {producto}")
print(f"Precio unitario: ${valor:,.2f}")
print(f"Cantidad: {cantidad}")
print(f"Subtotal: ${total_sin_descuento:,}")

if opcion == 1:
    print(f"Descuento ({descuento}%): -${monto_descuento:,.2f}")

print(f"TOTAL A PAGAR: ${total_con_descuento:,.2f}")
print("-------------------------")

