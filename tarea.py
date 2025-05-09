# #Creo la lista de signo zodiacal con las tuplas de laa siguiente manera:
# #("nombre del signo",((dia_inicio,dia_fin),(mes_inicio,mes_final)))
# signo_zodiacal = [
#  ("Capricornio", (22, 12), (19, 1)),
#     ("Acuario", (20, 1), (18, 2)),
#     ("Piscis", (19, 2), (20, 3)),
#     ("Aries", (21, 3), (19, 4)),
#     ("Tauro", (20, 4), (20, 5)),
#     ("Géminis", (21, 5), (20, 6)),
#     ("Cáncer", (21, 6), (22, 7)),
#     ("Leo", (23, 7), (22, 8)),
#     ("Virgo", (23, 8), (22, 9)),
#     ("Libra", (23, 9), (22, 10)),
#     ("Escorpio", (23, 10), (21, 11)),
#     ("Sagitario", (22, 11), (21, 12))
# ]

# # Lo que le va a salir al usuario a la hora de ingresar su numero de dia y mes este ultimo que lo coloque en numeros
# while True:
#     try:
#         dia  = int(input("Ingrese su dia de nacimiento: "))
#         break
#     #Coloco todos los escenarios posibles adjuntandolos con or para que si cumple alguno de los requisitos pedidos los clasifico
#     except ValueError:
#         print("ingrese un numero de acuerdo a su dia de nacimiento")
        
# while True:
#     try:
#         mes = int(input("Ingrese su mes de nacimiento (en números): "))
#         break
#     #Coloco todos los escenarios posibles adjuntandolos con or para que si cumple alguno de los requisitos pedidos los clasifico
#     except ValueError:
#         print("ingrese un numero de acuerdo a tu mes de nacimeinto")
# #Creo un ciclo con for y les doy un valor a las variables de "inicio" y "fin"
# for signo_zodiacal, inicio, fin in signo_zodiacal:
#     dia_inicio, mes_inicio = inicio
#     dia_fin, mes_fin = fin

# if (mes == mes_inicio and dia >= dia_inicio) or (mes == mes_fin and dia <= dia_fin) or (mes_inicio < mes_fin and mes > mes_inicio and mes < mes_fin) or (mes_inicio > mes_fin and (mes > mes_inicio or mes < mes_fin))
#         print("Tu signo es:", signo_zodiacal)