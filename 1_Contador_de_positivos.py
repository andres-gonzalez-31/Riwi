# Plantea un programa que permita ingresar 10 números y cuente cuántos de ellos son mayores que cero.
print("bienvenido a tu contador."
      "\n 1.ingresa tus 10 valores"
      "\n 2. espera la respuesta para saber cual es mayor que 0.\n ")
contador_positivo =0
contador_negativo  =0


for i in range(1,11):
    notas_a_ingresar = int(input(f" ingresa tu {i}° nota : "))
    if notas_a_ingresar > 0:
        contador_positivo += 1
    elif notas_a_ingresar < 0:
        contador_negativo +=1

print(f"tus numeros mayor a cero son: {contador_positivo}")
print(f"tus numeros menor a cero son: {contador_negativo}")
        
        