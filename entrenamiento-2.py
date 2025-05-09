print("="*40)
print("Bienvenido a tu calculador de nota")
print("="*40,"\n")
lista_de_notas = []
# te pide que ingrese cuantas notas deseas ingresar solo con numeros, si ingresas un valor no numerico te manda un error
while True:
    try:
        notas_a_ingresar = int(input("cuantas notas deseas ingresar (ingresa un numero pos): "))
        if notas_a_ingresar > 0:
            break
        else:
            print("ERROR! ingresa un numero positivo\n")
    except:
        print("ERROR! ingresa nueva mente tu opcion\n") 

# te pido que ingreses tus notas de 0 a 100, despues de ingresar la nota te dice si es insuficiente, suficiente, bueno, muy bueno o sobresaliente
for i in range(notas_a_ingresar):
    while True:
        try:
            valor_de_nota = float(input(f"ingresa tu {i+1} nota: "))
            if  valor_de_nota >= 0  and valor_de_nota <=100:
                lista_de_notas.append(valor_de_nota)
                break
            else:
                print("ERROR!ingresa tu nota nueva mente")
        except:
            print("ERROR! ingresa un valor numerico valido")





# Calificacion de notas
    if valor_de_nota >= 0 and valor_de_nota < 59:
        print(f"😓 Insuficiente\n")
    elif (valor_de_nota >= 60 and valor_de_nota <= 69):
        print(f"🙂‍ Suficiente\n")
    elif (valor_de_nota >= 70 and valor_de_nota <= 79):
        print(f"👍 Bueno")
    elif (valor_de_nota >= 80 and valor_de_nota <= 89):
        print(f"🙌 Muy Bueno\n")
    elif (valor_de_nota >= 90 and valor_de_nota <= 100):
        print(f"🎊 Sobresaliente\n")
 
if valor_de_nota == 1:
    print(f"ingresaste una sola nota y es: {notas_a_ingresar}")
    print("finalizado el ingreso de notas")
    exit()
        
# si el valor de la nota es 1 se termina el ingreso de notas
promedio_de_nota = sum(lista_de_notas) / len(lista_de_notas) 
print("="*70)
print("Tus notas fueron recogidas y montadas en una lista. !EXITOSAMENRTE!.")  
print("="*70)
print(f"tu lista de notas es: {lista_de_notas}\n")

if promedio_de_nota < 50:
    print(f"tu promedio de notas es de: 😭 {promedio_de_nota:.2f}\n") 
elif 50 <= promedio_de_nota <65:  
    print(f"tu promedio de notas es de: 😱 {promedio_de_nota:.2f}\n") 
elif 65 <= promedio_de_nota <85:  
    print(f"tu promedio de notas es de: 🥱 {promedio_de_nota:.2f}\n") 
elif 85 <= promedio_de_nota <90:  
    print(f"tu promedio de notas es de: 🥳 {promedio_de_nota:.2f}\n") 
elif 90 <= promedio_de_nota <=100:  
    print(f"tu promedio de notas es de: 👑 {promedio_de_nota:.2f}\n") 
    
        
# Calificacion de notas

while True:
    try:
        lista_de_notas_entero = [int(x)  for x in lista_de_notas ]
        ingresa_numero_mayor_que = float(input(f"🔍 ingresa un valor numerico que este en tus notas.{lista_de_notas}"
                                               "\n para  saber cuales son mayor que este ingresa un numero entero. (entre 0 a 100): "))
        if 0 <=  ingresa_numero_mayor_que <=100:
            break
        else:
            print("ERROR!ingresa un valor entre 0 y 100")
    except:
        print("ERROR! ingresa un valor numerico valido")
    
while ingresa_numero_mayor_que == len(lista_de_notas_entero):
    break
else:
    print("este numero no se encuentra en la lista")
    exit()
      
    mayor_que = 0

    i = 0
    
    while i < len(lista_de_notas):
        if  lista_de_notas[i] > ingresa_numero_mayor_que:
            mayor_que += 1
        i +=1  
    print("="*70)
    print(f"hay ({mayor_que}) numeros mayores  que {ingresa_numero_mayor_que}")
    print("="*70)



while True:
    try:
        ingresa_numero_igual_que = float(input("🔍 acontinuacion ingresa un valor numerico que deses saber cuantas veces esta: "))
        if 0 <=  ingresa_numero_mayor_que <=100:
            break
        else:
            print("ERROR!ingresa un valor entre 0 y 100")
    except:
        print("ERROR! ingresa un valor numerico valido")


    