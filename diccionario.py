dicionario = {
    0 : "0",
    1 : "1",
    2 : "2",
    3 : "3",
    4 : "4",
    5 : "5",
    6 : "6",
    7 : "7",
    8 : "8",
    9 : "9",
    10 : "A",
    11 : "B",
    12 : "C",
    13 : "D",
    14 : "E",
    15 : "F"   
}

base = 16
hexadecimal = ""

valor = int(input("Ingrese un número decimal: "))

# Convertir un número decimal a hexadecimal
while valor > 0:
    resto = valor % base
    digito_hexadecimal = dicionario[resto]
    hexadecimal = digito_hexadecimal + hexadecimal
    valor = valor // base
print("El número en hexadecimal es:", hexadecimal)