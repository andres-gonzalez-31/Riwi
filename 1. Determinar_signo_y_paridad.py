while True:
    try:
        ingresa_numero_a_validar = int(input("ingresa tu numero a validar: "))
        break
    except:
        print("ERROR! ingresa un numero valido\n")
        
if ingresa_numero_a_validar > 0 and ingresa_numero_a_validar %2==0 :
    print(f"tu numero ({ingresa_numero_a_validar}) es par y positivo")
elif ingresa_numero_a_validar < 0 and ingresa_numero_a_validar %2==0 :
    print(f"tu numero ({ingresa_numero_a_validar}) es par y negativo")
elif ingresa_numero_a_validar > 0 and ingresa_numero_a_validar %2==1 :
    print(f"tu numero ({ingresa_numero_a_validar}) es inpar y positivo")
elif ingresa_numero_a_validar < 0 and ingresa_numero_a_validar %2==1 :
    print(f"tu numero ({ingresa_numero_a_validar}) es inpar y negativo")
else:
    print(f"tu numero es ({ingresa_numero_a_validar})")