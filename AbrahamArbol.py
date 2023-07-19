"""
1- Realizar una estructura de datos para representar el árbol genealógico de Abraham utilizando técnicas de POO, árboles y arrays. (30pts)
2- Recorrer el árbol genealógico de forma recursiva e ir mostrando a sus miembros por pantalla de forma clara y ordenada usando sangrías. (45pts)
3- Sacar un listado de todos los nombres ordenados alfabéticamente de forma ascendente. Utilice la estructura del árbol  como fuente de datos a procesar. 
En el proceso debe estar el algoritmo de ordenación llamado “Burbuja”. Se puede hacer uso de variables globales. (25pts)
"""

#Respuesta 1
class Tree:
    nombres = ""
    concubina = []
    hijos = []

    def __init__(self, n):
        self.nombre = n
        self.concubina = []
        self.hijos = []

node = Tree('Abraham')
node.concubina.append(Tree('Agar'))
node.concubina.append(Tree('Sara'))

node.concubina[0].hijos.append(Tree('Ismael'))
node.concubina[1].hijos.append(Tree('Isaac'))
node.concubina[1].hijos[0].concubina.append(Tree('Rebeca'))

node.concubina[1].hijos[0].concubina[0].hijos.append(Tree('Esau'))
node.concubina[1].hijos[0].concubina[0].hijos.append(Tree('Jacob'))
node.concubina[1].hijos[0].concubina[0].hijos[1].concubina.append(Tree('Lea'))

#Hijos Lea
node.concubina[1].hijos[0].concubina[0].hijos[1].concubina[0].hijos.append(Tree('Ruben'))
node.concubina[1].hijos[0].concubina[0].hijos[1].concubina[0].hijos.append(Tree('Simeon'))
node.concubina[1].hijos[0].concubina[0].hijos[1].concubina[0].hijos.append(Tree('Levi'))
node.concubina[1].hijos[0].concubina[0].hijos[1].concubina[0].hijos.append(Tree('Juda'))
node.concubina[1].hijos[0].concubina[0].hijos[1].concubina[0].hijos.append(Tree('Isacar'))
node.concubina[1].hijos[0].concubina[0].hijos[1].concubina[0].hijos.append(Tree('Zabulon'))

#Hijos Zilpa
node.concubuna[1].hijos[0].concubina[0].hijos[1].concubina[1].hijos.append(Tree('Gad'))
node.concubuna[1].hijos[0].concubina[0].hijos[1].concubina[1].hijos.append(Tree('Aser'))

#Hijos Raquel
node.concubina[1].hijos[0].concubina[0].hijos[1].concubina[2].hijos.append(Tree('Jose'))
node.concubina[1].hijos[0].concubina[0].hijos[1].concubina[2].hijos.append(Tree('Benjamin'))

#Hijos Bilha
node.concubina[1].hijos[0].concubina[0].hijos[1].concubina[3].hijos.append(Tree('Dan'))
node.concubina[1].hijos[0].concubina[0].hijos[1].concubina[3].hijos.append(Tree('Neftali'))

#Familia de José

node.concubina[1].hijos[0].concubina[0].hijos[1].concubina[2].hijos[0].concubina.append(Tree('Asenat'))
node.concubina[1].hijos[0].concubina[0].hijos[1].concubina[2].hijos[0].concubina[0].hijos.append(Tree('Manases'))
node.concubina[1].hijos[0].concubina[0].hijos[1].concubina[2].hijos[0].concubina[0].hijos.append(Tree('Efrain'))

#Respuesta 2: Recorrer el árbol genealógico de forma recursiva e ir mostrando a sus miembros por pantalla de forma clara y ordenada usando sangrías. (45pts)

def recorrido(r, sangria = ''):
    print(sangria + r.nombre)
    aux = sangria
    sangria += "   "
    for j in r.hijos:
        recorrido(j, sangria)
    for i in r.concubina:
        recorrido(i, aux)
    


# class Arbol: 
#     nombre = ''
#     concubina = []
#     hijos = []

#     def __init__(self, n):
#         self.nombre = n
#         self.concubina = []
#         self.hijos = []

# nodo = Arbol('Abraham')
# nodo.concubina.append(Arbol('Agar'))
# nodo.concubina.append(Arbol('Sara'))

# nodo.concubina[0].hijos.append(Arbol('Ismael'))
# nodo.concubina[1].hijos.append(Arbol('Isaac'))
# nodo.concubina[1].hijos[0].concubina.append(Arbol('Rebeca'))

# nodo.concubina[1].hijos[0].concubina[0].hijos.append(Arbol('Esau'))
# nodo.concubina[1].hijos[0].concubina[0].hijos.append(Arbol('Jacob'))
# nodo.concubina[1].hijos[0].concubina[0].hijos[1].concubina.append(Arbol('Lea'))
# nodo.concubina[1].hijos[0].concubina[0].hijos[1].concubina.append(Arbol('Zilpa'))
# nodo.concubina[1].hijos[0].concubina[0].hijos[1].concubina.append(Arbol('Raquel'))
# nodo.concubina[1].hijos[0].concubina[0].hijos[1].concubina.append(Arbol('Bilha'))

# # Hijos de Lea
# nodo.concubina[1].hijos[0].concubina[0].hijos[1].concubina[0].hijos.append(Arbol('Ruben'))
# nodo.concubina[1].hijos[0].concubina[0].hijos[1].concubina[0].hijos.append(Arbol('Simeon'))
# nodo.concubina[1].hijos[0].concubina[0].hijos[1].concubina[0].hijos.append(Arbol('Levi'))
# nodo.concubina[1].hijos[0].concubina[0].hijos[1].concubina[0].hijos.append(Arbol('Juda'))
# nodo.concubina[1].hijos[0].concubina[0].hijos[1].concubina[0].hijos.append(Arbol('Isacar'))
# nodo.concubina[1].hijos[0].concubina[0].hijos[1].concubina[0].hijos.append(Arbol('Zabulon'))

# # Hijos de Zilpa 
# nodo.concubina[1].hijos[0].concubina[0].hijos[1].concubina[1].hijos.append(Arbol('Gad'))
# nodo.concubina[1].hijos[0].concubina[0].hijos[1].concubina[1].hijos.append(Arbol('Aser'))

# # Hijos de Raquel 
# nodo.concubina[1].hijos[0].concubina[0].hijos[1].concubina[2].hijos.append(Arbol('Jose'))
# nodo.concubina[1].hijos[0].concubina[0].hijos[1].concubina[2].hijos.append(Arbol('Benjamin'))

# # Hijos de Bilha
# nodo.concubina[1].hijos[0].concubina[0].hijos[1].concubina[3].hijos.append(Arbol('Dan'))
# nodo.concubina[1].hijos[0].concubina[0].hijos[1].concubina[3].hijos.append(Arbol('Neftali'))

# # Familia Jose
# nodo.concubina[1].hijos[0].concubina[0].hijos[1].concubina[2].hijos[0].concubina.append(Arbol('Asenat'))
# nodo.concubina[1].hijos[0].concubina[0].hijos[1].concubina[2].hijos[0].concubina[0].hijos.append(Arbol('Manases'))
# nodo.concubina[1].hijos[0].concubina[0].hijos[1].concubina[2].hijos[0].concubina[0].hijos.append(Arbol('Efrain'))

def recorrer(r, sangria = ''):
    print(sangria + r.nombre)
    aux = sangria
    sangria += "   "
    for j in r.hijos: 
        recorrer(j, sangria)
    for i in r.concubina: 
        recorrer(i, aux)

recorrer(nodo)

def listar():
    nombres = []
    listarTodos(nodo, nombres)
    return nombres


def listarTodos(r, nombres):
    nombres.append(r.nombre)
    for j in r.hijos: 
        listarTodos(j, nombres)
    for i in r.concubina: 
        listarTodos(i, nombres)

def ordenar_burbuja(lista):
    for i in range(len(lista)-1):
        for j in range(len(lista)-i-1):
            if lista[j] > lista[j+1]:
                aux = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = aux
    return lista

print(ordenar_burbuja(listar()))