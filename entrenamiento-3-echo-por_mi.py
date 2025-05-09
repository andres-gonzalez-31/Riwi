 Hola Coder, en esta actividad vas a crear un programa en Python que simule cómo preparar distintas recetas de cocina.
# Para la presente actividad podrás utilizar todo lo aprendido en el módulo de Python. Principalmente deberás utilizar funciones, condicionales y estructuras como listas, tuplas o diccionarios para organizar los ingredientes y pasos de las recetas.
# 🎯 ¿Qué debes hacer?­
# Imagina que estás creando un asistente de cocina virtual. Este asistente debe saber preparar las siguientes tres recetas:
#     1. Ensalada César con pollo
#     2. Wrap de pollo con salsa César
#     3. Sándwich clásico de pollo


# guardar_datos_productos = []


# def ingresar_producto():
#     while True:
#         while True:
#             nombre_base = ''
#             nombre = input("🖊️ ingresa nombre del producto: ").lower()
#             if all(' ' != letra for letra in nombre) and nombre_base != nombre:
#                 break
#             else:
#                 print('💢ERROR! El nombre lleva espacios o está vacío, corrigelo!\n')
#                 continue
#         while True:
#             try:
#                 precio = float(input("💲 ingresa el precio del producto: "))
#                 if precio > 0:
#                     break
#                 else:
#                     print("💢ERROR! ingresa un numero positivo\n")
#                     continue
#             except ValueError:
#                 print("💢 ERROR! Ingresa un valor numerico\n")
#                 continue
#         while True:
#             try:
#                 cantidad = int(input("🛍️ ingresa la cantidad de producto a llevar: "))
#                 if cantidad > 0:
#                     break
#                 else:
#                     print("💢ERROR! ingresa un numero positivo\n")
#                     continue
#             except ValueError:
#                 print("💢 ERROR! Ingresa un valor numerico\n")
#                 continue
#         break
#     guardar_datos_diccionario = {"nombre": nombre,"precio": precio, "cantidad": cantidad}
#     guardar_datos_productos.append(guardar_datos_diccionario)
#     print(f"tu producto {nombre} con precio de {precio} un stok de {cantidad} fue guardado de manera exitosa")

# def consultar_producto ():
#    consultar_producto = input("ingresa nombre del producto a consultar: ").lower
#    for producto in guardar_datos_productos:
#        if producto["nombre"] == consultar_producto:
#            print(f"producto{consultar_producto}"
#                  f'\nprecio:{producto["precio"]:.2f}'
#                  f'\nprecio:{producto["cantidad"]}')

# def actualizar_precio_producto():
#     while True:    
#         ingresa_producto_actualizar = input("ingresa el nombre de producto para actualizar precio: ")
#         if ingresa_producto_actualizar.strip():
#             break
#         else:
#             print("💢ERROR! ingresa un nombre correcto\n")
#         if ingresa_producto_actualizar == guardar_datos_productos:
#                 print("estas seguro de cambiar el precio a este producto.")
#                 print("1.si")
#                 print("1.no")
#                 escoge_opcion = int(input("ingresa una opcion numerica.")) 
#                 if escoge_opcion == 1 or escoge_opcion <= 2:
#                     if escoge_opcion == 1:
#                         nuevo_precio = float(input(f"ingresa el nuevo precio del producto {ingresa_producto_actualizar}: "))
#                         guardar_datos_productos.append(nuevo_precio)
#                         break
#                     else:
#                         print("ok!")
#                 else:
#                     print("💢ERROR! ingresa un numero valido\n")
#         else:
#             print("💢ERROR! producto no encontrado\n")
                
# def eliminar_producto():
#     eliminar_producto = input("ingresa el nombre del producto a eliminar: ")
#     if eliminar_producto in guardar_datos_productos:
#         guardar_datos_productos.pop(eliminar_producto)
#     else:
#         print("💢ERROR! producto no encontrado\n")
# def calcular_inventario():
#     calcular_valor_total = lambda: sum(valor["valor"] * valor["stock"] for valor in guardar_datos_productos)
#     print(f"tu inventario actualmente tiene un valor de: {calcular_valor_total}")
# def menu():
#     while True:
#         try:
#             print("¨"*50)
#             print(("BIENVENIDO AL MENU DE INVENTARIO").center(50))
#             print("¨"*50)
#             print("selecciona 1. 📩 añaidr producto."
#                   "\nselecciona 2. 🖨️ consultar producto."
#                   "\nselecciona 3. 🗃️ actualizar precio de producto"
#                   "\nselecciona 4. 🗑️ eliminar producto"
#                   "\nselecciona 5. 📳 calcular valor total inventario"
#                   "\nselecciona 6. 📝 mostrar inventario completo"
#                   "\nselecciona 7. 🚪 salir")
#             selecciona_una_opcion = int(input("selecciona una opcion del menu: "))
#             if selecciona_una_opcion < 0:
#                 print("💢 ERROR! ingresa un numero positivo\n")
#                 continue
#         except ValueError:
#             print("💢 ERROR! Ingresa un valor numerico\n")
#         while True:
#             if selecciona_una_opcion == 1:
#                 print("-"*50)
#                 print("𝔹𝕚𝕖𝕟𝕧𝕖𝕟𝕚𝕕𝕠 𝕚𝕟𝕘𝕣𝕖𝕤𝕒 𝕝𝕒 𝕚𝕟𝕗𝕠𝕣𝕞𝕒𝕔𝕚𝕠𝕟 𝕕𝕖 𝕥𝕦 𝕡𝕣𝕠𝕕𝕦𝕔𝕥𝕠.")
#                 print("-"*50)
#                 ingresar_producto()
#                 print("🎉 INFORMACION INGRESADA CORRECTAMENTE.\n")
#             elif selecciona_una_opcion == 2:
#                 print("-"*70)
#                 print("𝔹𝕚𝕖𝕟𝕧𝕖𝕟𝕚𝕕𝕠. 𝕢𝕦𝕚𝕖𝕣𝕖𝕤 𝕔𝕠𝕟𝕤𝕦𝕝𝕥𝕒𝕣 𝕚𝕟𝕗𝕠𝕣𝕞𝕒𝕔𝕚𝕠𝕟 𝕤𝕠𝕓𝕣𝕖 𝕒𝕝𝕘𝕦𝕟 𝕡𝕣𝕠𝕕𝕦𝕔𝕥𝕠.")
#                 print("-"*70)
#                 consultar_producto()
#             elif selecciona_una_opcion == 3:
#                 print("-"*70)
#                 print("𝔹𝕚𝕖𝕟𝕧𝕖𝕟𝕚𝕕𝕠. 𝕢𝕦𝕚𝕖𝕣𝕖𝕤 actualizar precio 𝕤𝕠𝕓𝕣𝕖 𝕒𝕝𝕘𝕦𝕟 𝕡𝕣𝕠𝕕𝕦𝕔𝕥𝕠.")
#                 print("-"*70)
#                 actualizar_precio_producto()
#             elif selecciona_una_opcion == 4:
#                 print("-"*70)
#                 print("𝔹𝕚𝕖𝕟𝕧𝕖𝕟𝕚𝕕𝕠. 𝕢𝕦𝕚𝕖𝕣𝕖𝕤 eliminar 𝕒𝕝𝕘𝕦𝕟 𝕡𝕣𝕠𝕕𝕦𝕔𝕥𝕠.")
#                 print("-"*70)
#                 eliminar_producto()
#             elif selecciona_una_opcion == 5:
#                 print("-"*70)
#                 print("𝔹𝕚𝕖𝕟𝕧𝕖𝕟𝕚𝕕𝕠. 𝕢𝕦𝕚𝕖𝕣𝕖𝕤 eliminar 𝕒𝕝𝕘𝕦𝕟 𝕡𝕣𝕠𝕕𝕦𝕔𝕥𝕠.")
#                 print("-"*70)
#                 calcular_inventario()
#             elif selecciona_una_opcion == 6:
#                 print("-"*70)
#                 print("𝔹𝕚𝕖𝕟𝕧𝕖𝕟𝕚𝕕𝕠. 𝕢𝕦𝕚𝕖𝕣𝕖𝕤 eliminar 𝕒𝕝𝕘𝕦𝕟 𝕡𝕣𝕠𝕕𝕦𝕔𝕥𝕠.")
#                 print("-"*70)
#                 eliminar_producto()
#             elif selecciona_una_opcion == 7:
#                 print("-"*70)
#                 print("muchas gracias por usar nuestro menu.")
#                 print("-"*70)
#                 exit()
#             break
      

# menu()
#     while True:
#         print("\n*" * 50)
#         print(" BIENVENIDO AL MENU DE INVENTARIO ".center(50))
#         print("*" * 50)
#         print("Seleccione una opción:")
#         print("1. 📩 Añadir producto")
#         print("2. 🖨️ Consultar producto")
#         print("3. 🗃️ Actualizar precio de producto")
#         print("4. 🗑️ Eliminar producto")
#         print("5. 📳 Calcular valor total inventario")
#         print("6. 📝 Mostrar inventario completo")
#         print("7. 🚪 Salir")
#         print("*" * 50)
#         try:
#             seleccion = int(input("Seleccione una opción del menú: "))
#             if 1 <= seleccion <= 7:
#                 break # Rompe el bucle si la entrada es válida
#             else:
#                 print("💢 ERROR! Ingrese un número entre 1 y 7.\n")
#         except ValueError:
#             print("💢 ERROR! Ingrese un valor numérico válido.\n")

#     while True:
#         if seleccion == 1:
#             print("-" * 50)
#             print(" 𝔹𝕚𝕖𝕟𝕧𝕖𝕟𝕚𝕕𝕠 𝕒 𝕝𝕒 𝕤𝕖𝕔𝕔𝕚ó𝕟 𝕕𝕖 𝕒ñ𝕒𝕕𝕚𝕣 𝕡𝕣𝕠𝕕𝕦𝕔𝕥𝕠. ".center(50, "-"))
#             print("-" * 50)
#             ingresar_producto()
#             print("🎉 Producto ingresado correctamente.\n")
#         elif seleccion == 2:
#             print("-" * 50)
#             print(" 𝔹𝕚𝕖𝕟𝕧𝕖𝕟𝕚𝕕𝕠 𝕒 𝕝𝕒 𝕤𝕖𝕔𝕔𝕚ó𝕟 𝕕𝕖 𝕔𝕠𝕟𝕤𝕦𝕝𝕥𝕒𝕣 𝕡𝕣𝕠𝕕𝕦𝕔𝕥𝕠. ".center(50, "-"))
#             print("-" * 50)
#             consultar_producto()
#         elif seleccion == 3:
#             print("-" * 50)
#             print(" 𝔹𝕚𝕖𝕟𝕧𝕖𝕟𝕚𝕕𝕠 𝕒 𝕝𝕒 𝕤𝕖𝕔𝕔𝕚ó𝕟 𝕕𝕖 𝕒𝕔𝕥𝕦𝕒𝕝𝕚𝕫𝕒𝕣 𝕡𝕣𝕖𝕔𝕚𝕠. ".center(50, "-"))
#             print("-" * 50)
#             actualizar_precio_producto()
#         elif seleccion == 4:
#             print("-" * 50)
#             print(" 𝔹𝕚𝕖𝕟𝕧𝕖𝕟𝕚𝕕𝕠 𝕒 𝕝𝕒 𝕤𝕖𝕔𝕔𝕚ó𝕟 𝕕𝕖 𝕖𝕝𝕚𝕞𝕚𝕟𝕒𝕣 𝕡𝕣𝕠𝕕𝕦𝕔𝕥𝕠. ".center(50, "-"))
#             print("-" * 50)
#             eliminar_producto()
#         elif seleccion == 5:
#             print("-" * 50)
#             print(" 𝔹𝕚𝕖𝕟𝕧𝕖𝕟𝕚𝕕𝕠 𝕒 𝕝𝕒 𝕤𝕖𝕔𝕔𝕚ó𝕟 𝕕𝕖 𝕔𝕒𝕝𝕔𝕦𝕝𝕒𝕣 𝕚𝕟𝕧𝕖𝕟𝕥𝕒𝕣𝕚𝕠. ".center(50, "-"))
#             print("-" * 50)
#             calcular_inventario()
#         elif seleccion == 6:
#             print("-" * 50)
#             print(" 𝔹𝕚𝕖𝕟𝕧𝕖𝕟𝕚𝕕𝕠 𝕒 𝕝𝕒 𝕤𝕖𝕔𝕔𝕚ó𝕟 𝕕𝕖 𝕞𝕠𝕤𝕥𝕣𝕒𝕣 𝕚𝕟𝕧𝕖𝕟𝕥𝕒𝕣𝕚𝕠. ".center(50, "-"))
#             print("-" * 50)
#             mostrar_inventario_completo()
#         elif seleccion == 7:
#             print("-" * 50)
#             print(" ¡𝔾𝕣𝕒𝕔𝕚𝕒𝕤 𝕡𝕠𝕣 𝕦𝕤𝕒𝕣 𝕟𝕦𝕖𝕤𝕥𝕣𝕠 𝕤𝕚𝕤𝕥𝕖𝕞𝕒 𝕕𝕖 𝕚𝕟𝕧𝕖𝕟𝕥𝕒𝕣𝕚𝕠! ".center(50, "-"))
#             print("-" * 50)
#             exit()
#         break
    
# guardar_datos_productos = []
# # Ejecutar el menú principal
# menu()
