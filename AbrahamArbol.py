class Arbol: 
    nombre = ''
    concubina = []
    hijos = []

    def __init__(self, n):
        self.nombre = n
        self.concubina = []
        self.hijos = []

nodo = Arbol('Abraham')
nodo.concubina.append(Arbol('Agar'))
nodo.concubina.append(Arbol('Sara'))

nodo.concubina[0].hijos.append(Arbol('Ismael'))
nodo.concubina[1].hijos.append(Arbol('Isaac'))
nodo.concubina[1].hijos[0].concubina.append(Arbol('Rebeca'))

nodo.concubina[1].hijos[0].concubina[0].hijos.append(Arbol('Esau'))
nodo.concubina[1].hijos[0].concubina[0].hijos.append(Arbol('Jacob'))
nodo.concubina[1].hijos[0].concubina[0].hijos[1].concubina.append(Arbol('Lea'))
nodo.concubina[1].hijos[0].concubina[0].hijos[1].concubina.append(Arbol('Zilpa'))
nodo.concubina[1].hijos[0].concubina[0].hijos[1].concubina.append(Arbol('Raquel'))
nodo.concubina[1].hijos[0].concubina[0].hijos[1].concubina.append(Arbol('Bilha'))

# Hijos de Lea
nodo.concubina[1].hijos[0].concubina[0].hijos[1].concubina[0].hijos.append(Arbol('Ruben'))
nodo.concubina[1].hijos[0].concubina[0].hijos[1].concubina[0].hijos.append(Arbol('Simeon'))
nodo.concubina[1].hijos[0].concubina[0].hijos[1].concubina[0].hijos.append(Arbol('Levi'))
nodo.concubina[1].hijos[0].concubina[0].hijos[1].concubina[0].hijos.append(Arbol('Juda'))
nodo.concubina[1].hijos[0].concubina[0].hijos[1].concubina[0].hijos.append(Arbol('Isacar'))
nodo.concubina[1].hijos[0].concubina[0].hijos[1].concubina[0].hijos.append(Arbol('Zabulon'))

# Hijos de Zilpa 
nodo.concubina[1].hijos[0].concubina[0].hijos[1].concubina[1].hijos.append(Arbol('Gad'))
nodo.concubina[1].hijos[0].concubina[0].hijos[1].concubina[1].hijos.append(Arbol('Aser'))

# Hijos de Raquel 
nodo.concubina[1].hijos[0].concubina[0].hijos[1].concubina[2].hijos.append(Arbol('Jose'))
nodo.concubina[1].hijos[0].concubina[0].hijos[1].concubina[2].hijos.append(Arbol('Benjamin'))

# Hijos de Bilha
nodo.concubina[1].hijos[0].concubina[0].hijos[1].concubina[3].hijos.append(Arbol('Dan'))
nodo.concubina[1].hijos[0].concubina[0].hijos[1].concubina[3].hijos.append(Arbol('Neftali'))

# Familia Jose
nodo.concubina[1].hijos[0].concubina[0].hijos[1].concubina[2].hijos[0].concubina.append(Arbol('Asenat'))
nodo.concubina[1].hijos[0].concubina[0].hijos[1].concubina[2].hijos[0].concubina[0].hijos.append(Arbol('Manases'))
nodo.concubina[1].hijos[0].concubina[0].hijos[1].concubina[2].hijos[0].concubina[0].hijos.append(Arbol('Efrain'))

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