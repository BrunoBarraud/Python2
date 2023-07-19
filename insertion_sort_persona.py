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


def insertion_sort(array):

    for step in range(1, len(array)):
        key = array[step]
        j = step - 1
              
        #Iterara e ir comparando el valor rescatado con cada elemento de la izquierda
        #hasta encontrar un valor menor a este
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        
        # Ubicar el valor rescatado justo por delante del valor menor a este
        array[j + 1] = key

personas = [Persona("Maria",10), Persona("Zoel",5), Persona("Pedro",45), Persona("Paulo",33)]
print('Personas Antes Ordenación: ')
##esta funcion imprime el array
#print(personas)
#para imprimir el array como atributos de la función print usamos *
print(*personas)
insertion_sort(personas)

print("\nPersonas Después Ordenación: ")
print(*personas)

