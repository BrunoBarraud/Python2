print("Ejemplo básico de Listas enlazadas con POO en Python")
print("---")

# class Letra:
#     siguiente_letra = None
#     def __init__(self, letra):
#         self.letras = letra
    
# raiz = Letra("A")

# raiz.siguiente_letra = Letra("B")

# raiz.siguiente_letra.siguiente_letra = Letra("C")

# def mostrar_lista(x):
#     while x != None:
#         print(x.letra)
#         x = x.siguiente_letra

# mostrar_lista(raiz)
   
    
"""
Práctica:
---------
1) Hacer una función para agregar un elemento más al final de la lista
2) Hacer una función para sacar un elemento al final de la lista
3) Hacer una función para sacar un elemento al comienzo de la lista
4) Hacer una función para sacar un elemento en la posición x de la lista
   (reenlazar los objetos detrás)
5) Hacer una función para agregar un elemento más en la posición x de la lista   
"""

#Inserta elemento al inicio de la lista
def agregar_elemento_inicio(lista, elemento):
    lista.insert(0, elemento)
    return lista
 # Ejemplo de uso
mi_lista = [1, 2, 3, 4]
nuevo_elemento = 0
mi_lista = agregar_elemento_inicio(mi_lista, nuevo_elemento)
print(mi_lista)


#Inserta elemento al final de la lista
def agregar_elemento_final(lista, elemento):
    lista.append(elemento)
    return lista
 # Ejemplo de uso
mi_lista = [1, 2, 3, 4]
nuevo_elemento = 0
mi_lista = agregar_elemento_final(mi_lista, nuevo_elemento)
print(mi_lista)

x = int(input("Inserte una posicion: "))

def agregar_elemento_posicionx(lista, elemento, x):
    lista.insert(x, elemento)
    return lista
 # Ejemplo de uso
mi_lista = [1, 2, 3, 4]
nuevo_elemento = 0
mi_lista = agregar_elemento_posicionx(mi_lista, nuevo_elemento, x)
print(mi_lista)

def sacar_elemento_inicio(lista):
    lista.pop(0)
    return lista
 # Ejemplo de uso
mi_lista = [1, 2, 3, 4]
nuevo_elemento = 0
mi_lista = sacar_elemento_inicio(mi_lista)
print(mi_lista)

agregar_elemento_inicio(mi_lista, nuevo_elemento)
agregar_elemento_final(mi_lista, nuevo_elemento)
agregar_elemento_posicionx(mi_lista, nuevo_elemento, x)
sacar_elemento_inicio(mi_lista) 

