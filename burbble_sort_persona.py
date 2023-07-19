class Persona:
    nome = None
    edad = None

    def __init__(self, nome, edad):
        self.nome = nome
        self.edad = edad

    def __str__(self):
        return self.nome + "," + str(self.edad)

    #llamado por el operador ==
    def __eq__(self, otra_persona):
        return self.nome == otra_persona.nome

    #llamado por el operador !=
    def __ne__(self, otra_persona):
        return self.nome != otra_persona.nome

    #llamado por el operador >
    def __gt__(self, otra_persona):
        return self.nome > otra_persona.nome

    #llamado por el operador <
    def __lt__(self, otra_persona):
        return self.nome < otra_persona.nome

    #llamado por el operador >=
    def __ge__(self, otra_persona):
        return self.nome >= otra_persona.nome

    #llamado por el operador <=
    def __le__(self, otra_persona):
        return self.nome <= otra_persona.nome


def ordenar_burbuja(lista):
    for i in range(len(lista)-1):
        for j in range(len(lista)-i-1):
            print("---")
            print("i: " + str(i) + " - j: " + str(j) + " => ", end=" ")
            print(*lista)
            print(str().rjust(j*3+16) + "-  -")
            if lista[j] > lista[j+1]:
                print("    Intercambiando: " + str(lista[j]) + " : " + str(lista[j+1]))
                #swap
                aux = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = aux
                #lista[j], lista[j+1] = lista[j+1], lista[j]
    

personas = [Persona("Maria",10), Persona("Zoel",5), Persona("Pedro",45), Persona("Paulo",33)]
print('Personas Antes Ordenación: ')
##esta funcion imprime el array
#print(personas)
#para imprimir el array como atributos de la función print usamos *
print(*personas)
ordenar_burbuja(personas)
print('Personas Después Ordenación: ')
print(*personas)

