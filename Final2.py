"""
 Mediana: muestra ordenada de menor a mayor, la mediana es el objeto del medio
    Final AyED
    14/12/2022
    
    Entregar el programa resuelto por email antes de las 11:30
    
    Sistema de cálculo de estadísticas climatológicas
    -------------------------------------------------
    Objetivo general: construir un sistema de carga y cálculo de información
    climática de ciudades del país.
    El sistema deberá considerar:
    1) la información de la ciudad debe estar construida con objetos con los 
       siguientes datos: nombre de la ciudad, un promedio anual de temperatura,
       temperatura máxima y mínima registrada
    2) las ciudades (objeto) será almacenadas y gestionadas en un array
    3) cuando arranca el sistema debe haber al menos 3 ciudades instanciadas
       dentro del array
    4) el sistema debe permitir, en un ciclo infinito, la carga de otra nueva 
       ciudad y agregado al array
    5) cada vez que se incorpora una nueva ciudad, se debe recalcular y mostrar:
        a) el promedio de temperatura del país. (de las temp promedio de cada ciudad)
        b) la mediana de temperatura (del promedio anual de ciudad) del país. 
           (cantidad de datos pares: entonces se hace un promedio entre los 
           datos centrales)
        c) ciudad más calurosa (de la temp max.)
        d) ciudad más fria (de la temp min.)
"""

# class Ciudad:
    
#     def __init__(self, nombre, prom_anual_temp, temp_max, temp_min):
#         self.nombre = nombre
#         self.prom_anual_temp = prom_anual_temp
#         self.temp_max = temp_max
#         self.temp_min = temp_min

#     def get_nombre(self):
#         return self.nombre
    
#     def get_temp(self):
#         return self.prom_anual_temp
    
#     def get_max(self):
#         return self.temp_max
    
#     def get_min(self):
#         return self.temp_min
    
#     def get_prom_temp(self, ciudades):
#         total_temperaturas = 0
#         acumulador = 0
#         for ciudad in ciudades:
#             total_temperaturas += ciudad.get_temp()
#             acumulador += 1
#         print("La temperatura promedio del pais es: ", round(total_temperaturas / acumulador, 1))

#     def get_max(self, ciudades):
#         t_max = 0
#         ciudad = ""
#         for i in ciudades:
#             if t_max < i.get_Max():
#                 t_max = i.get_Max()
#                 ciudad = i.get_nombre()
#             print("La temperatura máxima registrada es en ", ciudad, " y es de: ", t_max, "°")

#     def get_min(ciudades):
#             t_min = 100
#             ciudad = ""
#             for i in ciudades:
#                 if t_min > i.get_min():
#                     t_min = i.get_min()
#                     ciudad = i.get_nombre()
#                 print("La temperatura minima registrada es en ", ciudad, " y es de: ", t_min, "°")

#     def get_mediana(self, ciudades):
#             array = []
#             for i in ciudades:
#                 temperatura = i.get_temp()
#                 array.append(temperatura)
#             array.sort()
#             mediana = len(array)
#             if mediana % 2 == 0:
#                 resultado = (array[mediana // 2 - 1] + array[mediana // 2]) / 2
#             else:
#                 resultado = array[mediana // 2]
#             print("La mediana de temperatura es: ", resultado, "°")

#     def agregar_ciudad(self, nuevo_nombre, nuevo_prom_anual_temp, nuevo_temp_max, nuevo_temp_min, ciudades):
#         nueva_ciudad = Ciudad(nuevo_nombre, nuevo_prom_anual_temp, nuevo_temp_max, nuevo_temp_min)
#         ciudades.append(Ciudad(nuevo_nombre, nuevo_prom_anual_temp, nuevo_temp_max, nuevo_temp_min))
#         return ciudades

#     def menu(ciudades):
#         print("Seleccione una opción: ")
#         print("0 -> Salir del programa ")
#         print("1 -> Añadir ciudad ")
#         print("2 -> Calcular promedio de temperatura en el pais: ")
#         print("3 -> Calcular mediana de temperatura ")
#         print("4 -> Ciudad más calurosa ")
#         print("5 -> Ciudad más fría ")

#         op = input()

#         if op == '0':
#             print("Gracias por utilizar el programa ")
#             exit()
#         elif op == '1':
#             print("Escriba el nombre de la ciudad ")
#             nuevo_nombre = input()
#             print("Escriba el promedio de temperatura de la ciudad ")
#             temperatura_prom = float(input())
#             print("Escribe el máximo de temperatura registrada ")
#             max_reg = float(input())
#             print("Escribe el mínimo de temperatura registrada ")
#             min_reg = float(input())

#             agregar_ciudad(nuevo_nombre, temperatura_prom, max_reg, min_reg, ciudades)
#             menu(ciudades)

#         elif op == '2':
#             get_prom_temp(ciudades)
#             menu(ciudades)

#         elif op == '3':
#             get_mediana(ciudades)
#             menu(ciudades)

#         elif op == '4':
#             get_Max(ciudades)
#             menu(ciudades)

#         elif op == '5':
#             get_min(ciudades)
#             menu(ciudades)

#         else:
#             print("Por favor seleccione una opción correcta ")
#             menu(ciudades)


# ciudades = []
# menu(ciudades)


class Ciudad:
    def __init__(self, nom, prom_anual, temp_max, temp_min):
        self.nombre = nom
        self.prom_anual_temp = prom_anual
        self.temp_max = temp_max
        self.temp_min = temp_min

    def get_nom(self):
        return self.nombre

    def get_temp(self):
        return self.prom_anual_temp

    def get_max(self):
        return self.temp_max

    def get_min(self):
        return self.temp_min


def get_prom_temp(ciudades):
    total_temperaturas = 0
    acumulador = 0
    for i in ciudades:
        total_temperaturas += int(i.get_temp())
        acumulador += 1
    print(f"La temperatura promedio del país es: {round((total_temperaturas / acumulador), 1)}°")


def get_max(ciudades):
    t_max = 0
    ciudad = ""
    for i in ciudades:
        if t_max < int(i.get_max()):
            t_max = int(i.get_max())
            ciudad = i.get_nom()
    print(f"La temperatura máxima registrada es en {ciudad} y es de: {t_max}°")


def get_min(ciudades):
    t_min = 100
    ciudad = ""
    for i in ciudades:
        if t_min > int(i.get_min()):
           t_min = int(i.get_min())
           ciudad = i.get_nom()
    print(f"La temperatura mínima registrada es en {ciudad} y es de: {t_min}°")


def get_mediana(ciudades):
    array = []
    for i in ciudades:
        temperatura = i.get_temp()
        nombre = i.get_nom()
        array.append(temperatura)
    array.sort()
    mediana = len(array)
    resultado = ""
    if (mediana % 2) == 0:
        resultado = (array[int(mediana / 2)] + array[int(mediana / 2) + 1]) / 2
        print(f"La mediana de temperatura es: {resultado}°")
    else:
        resultado = array[int(round(mediana / 2))]
        print(f"La mediana de temperatura es: {resultado}°")


def menu():
    global ciudades
    print("Seleccione una opción:")
    print("0 -> Salir del programa")
    print("1 -> Añadir ciudad")
    print("2 -> Calcular promedio de temperatura en el país")
    print("3 -> Calcular mediana de temperatura")
    print("4 -> Ciudad más calurosa")
    print("5 -> Ciudad más fría")
    op = int(input())
    if op == 0:
        return
    elif op == 1:
        nuevo_nombre = input("Escriba el nombre de la ciudad: ")
        temperatura_prom = input("Escriba el promedio de temperatura de la ciudad: ")
        max_reg = input("Escriba el máximo de temperatura registrada: ")
        min_reg = input("Escriba el mínimo de temperatura registrada: ")
        agregar_array(nuevo_nombre, temperatura_prom, max_reg, min_reg)
        print("Ciudad cargada con éxito")
        menu()
    elif op == 2:
        get_prom_temp(ciudades)
        menu()
    elif op == 3:
        get_mediana(ciudades)
        menu()
    elif op == 4:
        get_max(ciudades)
        menu()
    elif op == 5:
        get_min(ciudades)
        menu()
    else:
        print("Por favor seleccione una opción correcta")
        menu()


def agregar_array(new_nombre, new_prom, new_temp_max, new_temp_min):
    global ciudades
    new_ciudad = Ciudad(new_nombre, new_prom, new_temp_max, new_temp_min)
    ciudades.append(new_ciudad)


ciudades = [
    Ciudad("Córdoba Capital", "20", "31", "2"),
    Ciudad("Justiniano Posse", "23", "33", "5"),
    Ciudad("Buenos Aires", "21", "30", "1")
]

menu()





    
