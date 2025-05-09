numeros_positivos = 0
numeros_negativos = 0
suma = 0
for i in range(1,11):
    num = int(input(f"Ingrese {i}  número: "))
    if num > 0:
        numeros_positivos += 1
    elif num < 0:
        numeros_negativos += 1
    suma += num

print("Cantidad de números positivos:", numeros_positivos)
print("Cantidad de números negativos:", numeros_negativos)
if suma > 0:
    promedio_todos = suma / numeros_positivos
    print("Promedio de números: ",promedio_todos )
else:
    print("No se ingresaron números.")