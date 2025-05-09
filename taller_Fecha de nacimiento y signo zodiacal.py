# Este código permite ingresar una fecha de nacimiento y devuelve el signo zodiacal correspondiente.
dia = int(input("Ingrese el día de nacimiento: "))
mes = int(input("Ingrese el mes de nacimiento (en numeros): "))

# Se utilizan condicionales para determinar el signo zodiacal según la fecha ingresada.
if (dia >=20 and mes == 1) or (dia <= 18 and mes == 2):
# Se verifica si la fecha es válida y se imprime el resultado.
    print("Su signo zodiacal es: Acuario") 
elif (dia >=19 and mes == 2) or (dia <= 20 and mes == 3):
    # Se verifica si la fecha es válida y se imprime el resultado.
    print("Su signo zodiacal es: Piscis")
elif (dia >=21 and mes == 3) or (dia <= 19 and mes == 4):
    # Se verifica si la fecha es válida y se imprime el resultado.
    print("Su signo zodiacal es: Aries")
elif (dia >=20 and mes == 4) or (dia <= 20 and mes == 5):
    # Se verifica si la fecha es válida y se imprime el resultado.
    print("Su signo zodiacal es: Tauro")
elif (dia >=21 and mes == 5) or (dia <= 20 and mes == 6):
    # Se verifica si la fecha es válida y se imprime el resultado.
    print("Su signo zodiacal es: Geminis")
elif (dia >=21 and mes == 6) or (dia <= 22 and mes == 7):
    # Se verifica si la fecha es válida y se imprime el resultado.
    print("Su signo zodiacal es: Cancer")
elif (dia >=23 and mes == 7) or (dia <= 22 and mes == 8):
    # Se verifica si la fecha es válida y se imprime el resultado.
    print("Su signo zodiacal es: Leo")
elif (dia >=23 and mes == 8) or (dia <= 22 and mes == 9):
    # Se verifica si la fecha es válida y se imprime el resultado.
    print("Su signo zodiacal es: Virgo")
elif (dia >=23 and mes == 9) or (dia <= 22 and mes == 10):
    # Se verifica si la fecha es válida y se imprime el resultado.
    print("Su signo zodiacal es: Libra")
elif (dia >=23 and mes == 10) or (dia <= 21 and mes == 11): 
    # Se verifica si la fecha es válida y se imprime el resultado.
    print("Su signo zodiacal es: Escorpio")
elif (dia >=22 and mes == 11) or (dia <= 21 and mes == 12):
    # Se verifica si la fecha es válida y se imprime el resultado.
    print("Su signo zodiacal es: Sagitario")
elif (dia >=22 and mes == 12) or (dia <= 19 and mes == 1):
    # Se verifica si la fecha es válida y se imprime el resultado.
    print("Su signo zodiacal es: Capricornio")
else:
    print("Fecha no válida")