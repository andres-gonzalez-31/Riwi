while True:
    try:
        print("ingresa una de las dos opciones"
              "\n1.si"
              "\n2.no")
        tu_dia_es_laborable = int(input("ingresa una opcion en numero: "))
        if tu_dia_es_laborable >0 and tu_dia_es_laborable <= 2:
            break
        else:
            print("ERROR! ingresa un numero valido (1 o 2)\n")
    except:
        print("ERROR! ingresa un numero\n ")
        
if tu_dia_es_laborable:
    horas_trabajadas = int(input("ingresa tu hora laborada: "))
    if (horas_trabajadas >=7 and horas_trabajadas <=9) or (horas_trabajadas >=17 and horas_trabajadas<=19):
        tarifa_a_pagar = horas_trabajadas * 7
        print(f"tu horas trabajadas fue de {horas_trabajadas} tu pago es de: {tarifa_a_pagar}pesos")
    else:
        tarifa_a_pagar = horas_trabajadas * 5
        print(f"tu horas trabajadas fue de {horas_trabajadas} tu pago es de:$ {tarifa_a_pagar}pesos")
else:
    print("FIN DE SEMANA")
    print("tu tarifa es de 0 pesos")