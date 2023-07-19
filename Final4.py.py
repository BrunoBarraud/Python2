class Client: 
    def __init__(self, i, n):
        self.id = i
        self.name = n
        self.left = None
        self.right = None

raiz = Client(1, 'Juan')
raiz.left = Client(2, 'Maria')
raiz.left.left = Client(9, 'Norma')
raiz.left.left.left = Client(8, 'Silvina')
raiz.left.right = Client(5, 'Karina')
raiz.right = Client(6, 'Diego')
raiz.right.left = Client(4, 'Ivana')
raiz.right.right = Client(3, 'Carlos')
raiz.right.right.right = Client(7, 'Ariel')

def imprimir_nombres_alfabeticamente(raiz) :
    if raiz: 
        imprimir_nombres_alfabeticamente(raiz.left)
        print (raiz.name, end=" ")
        imprimir_nombres_alfabeticamente(raiz.right)
imprimir_nombres_alfabeticamente(raiz)

print('\n----------------------------')

buscar = input('Escribir el nombre que se quiere buscar: ')

def encontrar(r, n):
    if r:
        if r.name == n:
            return r
        if encontrar(r.left, n):
            return r.left
        if encontrar(r.right, n):
            return r.right

print(encontrar(raiz, buscar))
print('----------------------------')

listaa = [raiz, raiz.left, raiz.left.left, raiz.left.left.left, raiz.left.right, raiz.right, raiz.right.left, raiz.right.right, raiz.right.right.right]

def ordenar_burbuja(lista):
    for i in range(len(lista)-1):
        for j in range(len(lista)-i-1):
            if lista[j].name > lista[j+1].name:
                aux = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = aux
    return lista

def imprimir_lista_ordenada():
    for i in ordenar_burbuja(listaa):
        print(str(i.id) + ': ' + i.name)

imprimir_lista_ordenada()

