# numero_entero = 12

# tipo_de_dato = type(numero_entero).__name__
# print("El tipo de dato de la variable numero_entero es:", tipo_de_dato)

# if tipo_de_dato == "int":
#     print("el dato es correcto.")
# else:
#     print("el dato es incorrecto.")

numero_entero = input("Ingrese un valor numerico: ")
numero_entero2 = input("Ingrese un segundo valor numerico: ")
contador = 0


try:
    numero_entero = int(numero_entero)
except:
    print("El valor ingresado no es un número entero.")
contador += 1

try:
    numero_entero2 = int(numero_entero2)
except:
    print("El valor ingresado no es un número entero.")
contador += 1

print("la cantidad de errores es:", contador)

tipo_de_dato = type(numero_entero).__name__
print("El tipo de dato de la variable numero_entero es:", tipo_de_dato)

tipo_de_dato2 = type(numero_entero2).__name__
print("El tipo de dato de la variable numero_entero es:", tipo_de_dato2)

if tipo_de_dato == "int":
    print("el dato es correcto.")
else:
    print("el dato es incorrecto.")
