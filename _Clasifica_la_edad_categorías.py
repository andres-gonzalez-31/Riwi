while True:
    try:
        ingresa_edad = int(input("ingresa tu edad: "))
        if ingresa_edad > 0:
            break
        else:
            print("ERROR! ingresa un numero positivo\n")
    except:
        print("ERROR! ingresa un numero valido\n")
        
if ingresa_edad < 18:
    print("eres Menor de edad :(")
elif ingresa_edad >=18 and ingresa_edad <=30:
    print("eres adulto joven :)")
elif ingresa_edad >=31 and ingresa_edad <=65:
    print("eres Adulto maduro ;)")
else:
    print("eres Adulto mayor <3")