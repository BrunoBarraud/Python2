print("Ejemplo básico de Listas enlazadas con POO en Python")
print("---")

class Letra:
    siguiente_letra = None

    def __init__(self, letra):
        self.letras = letra

    def __str__(self):
        return f'La Letra: {self.letras}'

def agregar_inicio(x):
    # 1) Cria una nueva letra
    global raiz
    nuevaRaiz = Letra(x)
    # 2) Faz com que o novo nodo seja a cabeça da lista.
    nuevaRaiz.siguiente_letra = raiz
    # 3) Faz com que a cabeça da lista referencie o novo nodo.
    raiz=nuevaRaiz

def agregar_fin(x):
    global raiz
    i=raiz
    #busca el fin
    while i.siguiente_letra != None:
        i = i.siguiente_letra

    #agrega la letra en fin
    i.siguiente_letra = Letra(x)

#agrega la letra 'x' en la posicion 'p' o en fin se la posicion no existe
def agregar_posicion(x, p):
    global raiz
    i=raiz
    posicion=1
    anterior=None
    #busca la posicion donde agregar
    while i.siguiente_letra != None and posicion!=p:
        anterior = i
        i = i.siguiente_letra
        posicion+=1

    #agrega la letra en fin incluso si la posicion no existe en la lista
    if i.siguiente_letra == None:
        i.siguiente_letra=Letra(x)
    #agrega en principio
    elif p==1:
        agregar_inicio(x)
    #agrega nel medio
    else:
        node = Letra(x)
        node.siguiente_letra = anterior.siguiente_letra
        anterior.siguiente_letra = node

def mostrar_lista(x):
    lista=""
    while x != None:
        lista+=x.letra +"->"
        x = x.siguiente_letra
    print (lista)

raiz = Letra("A")
agregar_inicio("B")
mostrar_lista(raiz)
agregar_fin("C")
mostrar_lista(raiz)
agregar_posicion("D",1)
agregar_posicion("E",2)
agregar_posicion("F",4)

mostrar_lista(raiz)

print("Raiz " + str(raiz))



"""
Práctica:
---------
1) Hacer una función para agregar un elemento más al final de la lista
2) Hacer una función para agregar un elemento más al inicio de la lista
3) Hacer una función para agregar un elemento más en la posición x de la lista

4) Hacer una función para sacar un elemento al final de la lista
5) Hacer una función para sacar un elemento al comienzo de la lista
6) Hacer una función para sacar un elemento en la posición x de la lista
   (reenlazar los objetos detrás)

"""

#Funcion para agregar un elemento mas al final de la lista

def agregar_elemento_final(lista, elemento):
    lista.append(elemento)
    return lista 

#Funcion para agregar un elemento mas al inicio de la lista

def agregar_elemento_inicio(lista, elemento):
    lista.insert(0, elemento)
    return lista

#Funcion para agregar un elemento mas en la posicion x de la lista

x = int(input("Inserte una posicion: "))

def agregar_elemento_inicio_posicionx(lista, elemento, x):
    lista.insert(x, elemento)
    return lista

#Funcion para sacar un elemento al final de la lista

def quitar_elemento_inicio_lista(lista, elemento):
    lista.pop(0, elemento)
    return lista

def quitar_elemento_final_lista(lista, elemento):
    lista.pop(-1, elemento)
    return lista

