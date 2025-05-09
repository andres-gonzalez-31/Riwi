# edad = int(input("ingresa tu edad: "))

# resta = 18 - edad

# if edad < 18:
#     print(f"te faltan {resta} años, no puedes votar")
# else:
#     print("estas listos para votar")

def procesar_datos():
    nombre=input("Ingrese nombre: ")
    while True:
        edad=input("Edad: ")
        if edad.isdigit():
            edad=int(edad)
            if edad>17:
                print(f"{nombre} tienes {edad} eres Mayor de edad")
            else:
                print(f"{nombre} tienes {edad} eres Menor de edad")
        else:
            print("Edad inválida, ingrese un numero")

procesar_datos()


# suma = 0
# while True:
#     entrada = input("Introduce un número o 's' para salir: ")
#     if entrada.lower() == 's':
#         break
#     try:
#         numero = int(entrada)
#         suma += numero
#     except ValueError:
#         print("Por favor ingresa un número válido o 's' para salir.")
        
# print("La suma es:", suma)

# Pedir los dos primeros números obligatoriamente
# numero1 = int(input("Introduce el primer número: "))
# numero2 = int(input("Introduce el segundo número: "))
# suma = numero1 + numero2

# # A partir del tercer número, dar opción de salir
# while True:
#     opcion = input("¿Quieres ingresar otro número? (s/n): ")
#     if opcion.lower() == 'n':
#         break
#     else:
#         numero = int(input("Introduce el siguiente número: "))
#         suma += numero

# print("La suma de los números es:", suma)

