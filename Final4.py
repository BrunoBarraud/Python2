"""
1) Recorrer el arbol e imprimir en orden ascendente, sin modificar el arbol ni utilizar un metodo de ordenación
2) Hacer una funcion que reciba como parámetro un nombre para buscar y que devuelva el objeto o, en caso de que no esté un None
3) Hacer una lista de los objetos y ordenar los nombres utilizando el metodo de burbuja

"""
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

print("----------------------------")

def print_names_inorder(root):
    if root:
        print_names_inorder(root.right)
        print(root.name, end=" ")
        print_names_inorder(root.left)
print_names_inorder(raiz)


print('\n----------------------------')

buscar = input('Escribir el nombre que se quiere buscar: ')

def buscar_nombre(root, buscar):
    if root == None:
        print('No se encontró el nombre')
    else:
        buscar_nombre(root.right, buscar)
        if root.name.lower() == buscar.lower():
            print(root.name + ' encontrado')
        buscar_nombre(root.left, buscar)
buscar_nombre(raiz, buscar)






lista = [raiz, raiz.left, raiz.left.left, raiz.left.left.left, raiz.left.right, raiz.right, raiz.right.left, raiz.right.right, raiz.right.right.right]

def ordenar_burbuja(lista):
    for i in range(len(lista)-1):
        for j in range(len(lista)-i-1):
            if lista[j].name > lista[j+1].name:
                aux = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = aux
    return lista

def imprimir_lista_ordenada():
    for i in ordenar_burbuja(lista):
        print(str(i.id) + ': ' + i.name)

imprimir_lista_ordenada()

