while True:
    try:
        valor_a_descontar = int(input("ingresa el valor de tu compra: "))
        if valor_a_descontar > 0:
            break
        else:
            print("ERROR! ingresa un valor positivo\n")
    except:
        print("ERROR! ingresa un valor numerico\n")

while True:
    try:
        print("que tipo de cliente eres."
              "\n1.vip"
              "\n2.no vip")
        tipo_de_cliente = int(input("ingresa un numero: "))
        if tipo_de_cliente > 0 and tipo_de_cliente <=2:
            break
        else:
            print("ERROR! ingresa un numero valido\n")
    except:
        print("ERROR! ingresa un valor numerico\n")
        
if tipo_de_cliente == 1:
    if valor_a_descontar >= 500:
        descuento = valor_a_descontar * 0.20
        total_a_pagar = valor_a_descontar - descuento
        print(f"tu valor a pagar es de: {total_a_pagar} ")
    else:
        descuento = valor_a_descontar * 0.10
        total_a_pagar = valor_a_descontar - descuento
        print(f"tu valor a pagar es de: {total_a_pagar} ")
else:
    if valor_a_descontar >= 500:
        descuento = valor_a_descontar * 0.05
        total_a_pagar = valor_a_descontar - descuento
        print(f"tu valor a pagar es de: {total_a_pagar} ")
    else:
        print(f"tu valor a pagar es de: {valor_a_descontar}")
        