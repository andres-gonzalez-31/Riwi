guardar_datos_productos = []

def ingresar_producto():
    """
    Función para ingresar los datos de un producto, incluyendo nombre, precio y cantidad.
    Maneja errores de entrada y asegura que los datos ingresados sean válidos.
    Guarda los datos en un diccionario y lo agrega a una lista global.
    """
    global guardar_datos_productos  # Declara que la variable es global

    while True:
        nombre_base = ''
        nombre = input("🖊️ ingresa nombre del producto: ").lower()
        if all(' ' != letra for letra in nombre) and nombre_base != nombre:
            break
        else:
            print('💢ERROR! El nombre lleva espacios o está vacío, corrigelo!\n')
            continue
        
    while True:
        try:
            precio = float(input("💲 ingresa el precio del producto: "))
            if precio > 0:
                break
            else:
                print("💢ERROR! ingresa un numero positivo\n")
                continue
        except ValueError:
            print("💢 ERROR! Ingresa un valor numerico\n")
            continue
        
    while True:
        try:
            cantidad = int(input("🛍️ ingresa la cantidad de producto a llevar: "))
            if cantidad > 0:
                break
            else:
                print("💢ERROR! ingresa un numero positivo\n")
                continue
        except ValueError:
            print("💢 ERROR! Ingresa un valor numerico\n")
            continue
    
    guardar_datos_diccionario = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
    guardar_datos_productos.append(guardar_datos_diccionario)
    print(f"Tu producto {nombre} con precio de {precio:.2f} y un stock de {cantidad} fue guardado de manera exitosa.")

def consultar_producto():
    """
    Función para consultar un producto por nombre.
    Muestra el nombre, precio y cantidad del producto si se encuentra.
    """
    consultar_nombre = input("Ingresa nombre del producto a consultar: ").lower()
    encontrado = False
    for producto in guardar_datos_productos:
        if producto["nombre"] == consultar_nombre:
            print("-" * 30)
            print(f"Producto: {producto['nombre'].capitalize()}")
            print(f"Precio: ${producto['precio']:.2f}")
            print(f"Cantidad en Stock: {producto['cantidad']}")
            print("-" * 30)
            encontrado = True
            break # Importante: Salir del bucle for si se encuentra el producto
    if not encontrado:
        print("💢 ERROR! Producto no encontrado.\n")

def actualizar_precio_producto():
    """
    Función para actualizar el precio de un producto existente.
    Pide el nombre del producto a actualizar, verifica que exista,
    y luego pide el nuevo precio.
    """
    nombre_producto_actualizar = input("Ingresa el nombre del producto para actualizar el precio: ").lower()
    encontrado = False
    for producto in guardar_datos_productos:
        if producto["nombre"] == nombre_producto_actualizar:
            encontrado = True
            while True:
                try:
                    nuevo_precio = float(input(f"Ingresa el nuevo precio del producto {nombre_producto_actualizar.capitalize()}: "))
                    if nuevo_precio > 0:
                        producto["precio"] = nuevo_precio # Actualiza el precio en el diccionario
                        print(f"Precio del producto {nombre_producto_actualizar.capitalize()} actualizado a ${nuevo_precio:.2f} exitosamente.")
                        break # Salir del bucle while
                    else:
                        print("💢 ERROR! Ingresa un número positivo\n")
                except ValueError:
                    print("💢 ERROR! Ingresa un valor numérico válido\n")
            break # Salir del bucle for
    if not encontrado:
        print("💢 ERROR! Producto no encontrado.\n")

def eliminar_producto():
    """
    Función para eliminar un producto de la lista.
    Pide el nombre del producto a eliminar y lo elimina si existe.
    """
    nombre_producto_eliminar = input("Ingresa el nombre del producto a eliminar: ").lower()
    encontrado = False
    for producto in guardar_datos_productos:
        if producto["nombre"] == nombre_producto_eliminar:
            guardar_datos_productos.remove(producto) # Elimina el producto de la lista
            print(f"Producto {nombre_producto_eliminar.capitalize()} eliminado exitosamente.")
            encontrado = True
            break # Salir del bucle for
    if not encontrado:
        print("💢 ERROR! Producto no encontrado.\n")

def calcular_inventario():
    """
    Función para calcular el valor total del inventario.
    Calcula el valor total multiplicando el precio por la cantidad de cada producto
    y sumando los resultados.
    """
    valor_total = 0
    for producto in guardar_datos_productos:
        valor_total += producto["precio"] * producto["cantidad"]
    print(f"El valor total del inventario es: ${valor_total:.2f}")

def mostrar_inventario_completo():
    """
    Función para mostrar el inventario completo.
    Muestra el nombre, precio y cantidad de todos los productos en la lista.
    """
    if not guardar_datos_productos:
        print("El inventario está vacío.\n")
        return  # Salir de la función si el inventario está vacío

    print("-" * 40)
    print("Inventario Completo")
    print("-" * 40)
    for producto in guardar_datos_productos:
        print(f"Producto: {producto['nombre'].capitalize()}")
        print(f"Precio: ${producto['precio']:.2f}")
        print(f"Cantidad en Stock: {producto['cantidad']}")
        print("-" * 40)


    """
    Función que muestra el menú principal y permite al usuario interactuar
    con las diferentes opciones del sistema de inventario.
    """
def menu():
    while True:
        try:
            print("¨"*50)
            print(("BIENVENIDO AL MENU DE INVENTARIO").center(50))
            print("¨"*50)
            print("selecciona 1. 📩 añaidr producto."
                  "\nselecciona 2. 🖨️ consultar producto."
                  "\nselecciona 3. 🗃️ actualizar precio de producto"
                  "\nselecciona 4. 🗑️ eliminar producto"
                  "\nselecciona 5. 📳 calcular valor total inventario"
                  "\nselecciona 6. 📝 mostrar inventario completo"
                  "\nselecciona 7. 🚪 salir")
            selecciona_una_opcion = int(input("selecciona una opcion del menu: "))
            if selecciona_una_opcion < 0:
                print("💢 ERROR! ingresa un numero positivo\n")
                continue
        except ValueError:
            print("💢 ERROR! Ingresa un valor numerico\n")
        while True:
            if selecciona_una_opcion == 1:
                print("-"*50)
                print("𝔹𝕚𝕖𝕟𝕧𝕖𝕟𝕚𝕕𝕠 𝕚𝕟𝕘𝕣𝕖𝕤𝕒 𝕝𝕒 𝕚𝕟𝕗𝕠𝕣𝕞𝕒𝕔𝕚𝕠𝕟 𝕕𝕖 𝕥𝕦 𝕡𝕣𝕠𝕕𝕦𝕔𝕥𝕠.")
                print("-"*50)
                ingresar_producto()
                print("🎉 INFORMACION INGRESADA CORRECTAMENTE.\n")
            elif selecciona_una_opcion == 2:
                print("-"*70)
                print("𝔹𝕚𝕖𝕟𝕧𝕖𝕟𝕚𝕕𝕠. 𝕢𝕦𝕚𝕖𝕣𝕖𝕤 𝕔𝕠𝕟𝕤𝕦𝕝𝕥𝕒𝕣 𝕚𝕟𝕗𝕠𝕣𝕞𝕒𝕔𝕚𝕠𝕟 𝕤𝕠𝕓𝕣𝕖 𝕒𝕝𝕘𝕦𝕟 𝕡𝕣𝕠𝕕𝕦𝕔𝕥𝕠.")
                print("-"*70)
                consultar_producto()
            elif selecciona_una_opcion == 3:
                print("-"*70)
                print("𝔹𝕚𝕖𝕟𝕧𝕖𝕟𝕚𝕕𝕠. 𝕢𝕦𝕚𝕖𝕣𝕖𝕤 actualizar precio 𝕤𝕠𝕓𝕣𝕖 𝕒𝕝𝕘𝕦𝕟 𝕡𝕣𝕠𝕕𝕦𝕔𝕥𝕠.")
                print("-"*70)
                actualizar_precio_producto()
            elif selecciona_una_opcion == 4:
                print("-" * 50)
                print(" 𝔹𝕚𝕖𝕟𝕧𝕖𝕟𝕚𝕕𝕠 𝕒 𝕝𝕒 𝕤𝕖𝕔𝕔𝕚ó𝕟 𝕕𝕖 𝕖𝕝𝕚𝕞𝕚𝕟𝕒𝕣 𝕡𝕣𝕠𝕕𝕦𝕔𝕥𝕠. ".center(50, "-"))
                print("-" * 50)
                eliminar_producto()
            elif selecciona_una_opcion == 5:
                print("-" * 50)
                print(" 𝔹𝕚𝕖𝕟𝕧𝕖𝕟𝕚𝕕𝕠 𝕒 𝕝𝕒 𝕤𝕖𝕔𝕔𝕚ó𝕟 𝕕𝕖 𝕔𝕒𝕝𝕔𝕦𝕝𝕒𝕣 𝕚𝕟𝕧𝕖𝕟𝕥𝕒𝕣𝕚𝕠. ".center(50, "-"))
                print("-" * 50)
                calcular_inventario()
            elif selecciona_una_opcion == 6:
                print("-" * 50)
                print(" 𝔹𝕚𝕖𝕟𝕧𝕖𝕟𝕚𝕕𝕠 𝕒 𝕝𝕒 𝕤𝕖𝕔𝕔𝕚ó𝕟 𝕕𝕖 𝕞𝕠𝕤𝕥𝕣𝕒𝕣 𝕚𝕟𝕧𝕖𝕟𝕥𝕒𝕣𝕚𝕠. ".center(50, "-"))
                print("-" * 50)
                mostrar_inventario_completo()
            elif selecciona_una_opcion == 7:
                print("-" * 50)
                print(" ¡𝔾𝕣𝕒𝕔𝕚𝕒𝕤 𝕡𝕠𝕣 𝕦𝕤𝕒𝕣 𝕟𝕦𝕖𝕤𝕥𝕣𝕠 𝕤𝕚𝕤𝕥𝕖𝕞𝕒 𝕕𝕖 𝕚𝕟𝕧𝕖𝕟𝕥𝕒𝕣𝕚𝕠! ".center(50, "-"))
                print("-" * 50)
                exit()
            break
      

menu()
