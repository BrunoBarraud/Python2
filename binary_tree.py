
"""
class Node:
    valor = ""
    left = None
    right = None
    def __init__(self, valor):
        self.valor = valor
        
#crear arbol de las diapositivas de clase        
raiz = Node("F")

raiz.left = Node("B")
raiz.left.left = Node("A")
raiz.left.right = Node("D")
raiz.left.right.left = Node("C")
raiz.left.right.right = Node("E")

raiz.right = Node("G")
raiz.right.right = Node("I")
raiz.right.right.left = Node("H")

def inorden(n):
    #pasar por nodo izquierdo
    if(n.left):
        inorden(n.left)
    #visitar nodo
    print(n.valor)
    #pasar por nodo derecho
    if(n.right):
        inorden(n.right)
        
#test
inorden(raiz)

"""

#Ejercicio 1 

#1 Cuales son las secuencias de nodos que se encuentran al atravesar el siguiente arbol en inorden, preorden y postorden?

class Node:
    valor = ""
    left = None
    right = None
    def __init__(self, valor):
        self.valor = valor

#Creamos el arbol:

raiz = Node("8")

#Empezamos por la izquierda
raiz.left = Node("9")
raiz.left.left = Node("11")
raiz.left.left.left = Node("15")
raiz.left.left.left.left = Node("19")
raiz.left.left.right = Node("20")
raiz.left.left.right.right = Node("21")

raiz.left.right = Node("7")
raiz.left.right.left = Node("3")
raiz.left.right.left.left = Node("2")
raiz.left.right.right = Node("1")

#Seguimos con la derecha

raiz.right = Node("5")
raiz.right.left = Node("6")
raiz.right.left.left = Node("4")
raiz.right.left.left.left = Node("13")
raiz.right.left.right = Node("14")
raiz.right.left.right.right = Node("10")

raiz.right.right = Node("12")
raiz.right.right.left = Node("17")
raiz.right.right.left.left = Node("16")
raiz.right.right.right = Node("18")

#Creamos funcion de recorrido inorden

def inorden(n):
    #pasar por nodo izquierdo
    if(n.left):
        inorden(n.left)
    #visitar nodo
    print(n.valor)
    #pasar por nodo derecho
    if(n.right):
        inorden(n.right)
print(inorden(raiz))

#Creamos funcion de recorrido preorden

def preorden(n):
    #visitar nodo
    print(n.valor)
    #pasar por nodo izquierdo
    if(n.left):
        preorden(n.left)
    #pasar por nodo derecho
    if(n.right):
        preorden(n.right)

print(preorden(raiz))

#Creamos funcion de recorrido postorden

def postorden(n):
    #pasar por nodo izquierdo
    if(n.left):
        postorden(n.left)
    #pasar por nodo derecho
    if(n.right):
        postorden(n.right)
    #visitar nodo
    print(n.valor)

print(postorden(raiz))



