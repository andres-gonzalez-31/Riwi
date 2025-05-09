# len lo uso para cuando el usuario ingrese la contraseña y
# depende los caracteres que ingrese va seguir o no en este caso coloque que tiene que ser mayo o igual que 8

while True:
    contraseña_a_crear = input("ingresa tu contraseña nueva: ")
    if len(contraseña_a_crear) >= 8 and "@" in contraseña_a_crear:
        print("contraseña correcta")
        break
    else:
        print("ERROR! contraseña incorrecta")