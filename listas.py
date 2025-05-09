# lista = [1,4,True,"hola", 4,4,[2,4,"hola"]]
# print(lista)
# print(lista.count(4))
# print(lista[0])
# print(lista[2])
# print(lista[3])
# print(lista[4])
# lista.copy()
# print(lista)
# lista.reverse()
# print(lista)
# lista.clear()
# print(lista)
# print(lista[4(0)])
# print(lista[4(2)])

# de acuerdo a la guia elabora un ejercicio donde solicites una lista de n numeros y 
# elabora un menu con la declaración match y aplica los metodos de listas para python, 
# por ejemplo ordenar la lista de numeros, eliminar un numero de la lista, 
# insertas mas numeros la lista, etc

# 1. `append()`
# Este método se utiliza para agregar un elemento al final de la lista.
# mi_lista = [1, 2, 3]
# mi_lista.append(4)
# for elemento in mi_lista:
# print(elemento)


# 2. `extend()`
# Permite agregar múltiples elementos al final de la lista.
# mi_lista = [1, 2, 3]
# mi_lista.extend([4, 5, 6])
# for elemento in mi_lista:
# print(elemento)

# 3. `insert()`
# Este método se utiliza para insertar un elemento en una posición específica de la lista.
# mi_lista = [1, 2, 3]
# mi_lista.insert(1, 'nuevo')
# for elemento in mi_lista:
# print(elemento)

# 4. `remove()`
# Elimina la primera aparición de un elemento en la lista.
# mi_lista = [1, 2, 3, 2]
# mi_lista.remove(2)
# for elemento in mi_lista:
#     print(elemento)

# 5. `pop()`
# Elimina y devuelve el último elemento de la lista (o el elemento en la posición especificada).
# mi_lista = [1, 2, 3]
# ultimo_elemento = mi_lista.pop()
# print(f'Elemento eliminado: {ultimo_elemento}')
# for elemento in mi_lista:
# print(elemento)

# 6. `sort()`
# Ordena los elementos de la lista en su lugar.
# mi_lista = [3, 1, 2]
# mi_lista.sort()
# for elemento in mi_lista:
# print(elemento)

# 7. `reverse()`
# Invierte el orden de los elementos en la lista.
# mi_lista = [1, 2, 3]
# mi_lista.reverse()
# for elemento in mi_lista:
# print(elemento)

# 8. `index()`
# # Devuelve el índice de la primera aparición de un elemento.
# mi_lista = [1, 2, 3, 2]
# indice = mi_lista.index(2)
# print(f'Índice del elemento 2: {indice}')

# 9. `count()`
# Devuelve el número de veces que un elemento aparece en la lista.
# mi_lista = [1, 2, 2, 3]
# conteo = mi_lista.count(2)
# print(f'El número 2 aparece: {conteo} veces')


# para llamar un valor que esta dentro de una lista que dentro de esa lista tiene 3 o etc de sublistas
# se llama de la siguiente manera ya q    ue asi se lee en python
# Lista_compleja = [1,4, [2,[3, [4, 5]]],45]
# print(Lista_compleja[-2][1][1][0])


calcu = {
    "hola":{
        "1234":[
            {
                "motor":23,
                "color":"rojo"
            },
            {
                "motor":24,
                "color":"azul"
            }
        ]
    }
}

#para llamar un valor quye esta dentro de de un diccionario que esta dentro de una lista que esta dentro de un subdicionario que    
# esta dentro de un diccionario.
print(calcu["hola"]["1234"][0]["motor"])