from smn_data import estadisticas
import os
import platform
import random


# Datos reales obtenidos de: https://www.smn.gob.ar/descarga-de-datos
# Valores promedios mensuales por estación meteorológica desde 1981 a 2010
# (29 años)

# Estructura de datos:
# --------------------
# estadisticas =
#      {
#         'Estación' => 'Nombre de la estación',
# 	    'Temperatura (°C)' => array('Ene' => '12.8', 'Feb' => '12.5', 'Mar' => '12.4', 'Abr' => '10.9', 'May' => '6.9', 'Jun' => '4.4', 'Jul' => '4.1', 'Ago' => '6.7', 'Sep' => '9.3', 'Oct' => '11.7', 'Nov' => '12.8', 'Dic' => '13.2'),
# 	    'Temperatura máxima (°C)' => array('Ene' => '20.1', 'Feb' => '19.9', 'Mar' => '19.9', 'Abr' => '19.7', 'May' => '17.3', 'Jun' => '15.6', 'Jul' => '15.4', 'Ago' => '17.4', 'Sep' => '19.2', 'Oct' => '21.1', 'Nov' => '21.7', 'Dic' => '21.3'),
# 	    'Temperatura mínima (°C)' => array('Ene' => '7.4', 'Feb' => '7.0', 'Mar' => '6.3', 'Abr' => '2.8', 'May' => '-3.0', 'Jun' => '-6.2', 'Jul' => '-6.8', 'Ago' => '-4.2', 'Sep' => '-1.1', 'Oct' => '2.8', 'Nov' => '5.2', 'Dic' => '6.9'),
# 	    'Humedad relativa (%)' => array('Ene' => '65.3', 'Feb' => '64.1', 'Mar' => '62.4', 'Abr' => '48.2', 'May' => '34.6', 'Jun' => '31.1', 'Jul' => '30.1', 'Ago' => '31.7', 'Sep' => '34.4', 'Oct' => '45.3', 'Nov' => '52.3', 'Dic' => '59.2'),
# 	    'Velocidad del Viento (km/h)' => array('Ene' => '6.9', 'Feb' => '7.1', 'Mar' => '6.5', 'Abr' => '6.4', 'May' => '6.0', 'Jun' => '4.9', 'Jul' => '6.6', 'Ago' => '6.6', 'Sep' => '8.6', 'Oct' => '8.7', 'Nov' => '8.8', 'Dic' => '8.3'),
# 	    'Nubosidad total (octavos)' => array('Ene' => '5.2', 'Feb' => '4.8', 'Mar' => '4.1', 'Abr' => '2.7', 'May' => '1.8', 'Jun' => '1.6', 'Jul' => '1.4', 'Ago' => '1.6', 'Sep' => '2.0', 'Oct' => '3.0', 'Nov' => '3.6', 'Dic' => '4.5'),
# 	    'Precipitación (mm)' => array('Ene' => '97.5', 'Feb' => '68.4', 'Mar' => '55.9', 'Abr' => '8.2', 'May' => '1.0', 'Jun' => '0.5', 'Jul' => '0.0', 'Ago' => '1.4', 'Sep' => '3.5', 'Oct' => '16.0', 'Nov' => '27.3', 'Dic' => '71.9'),
# 	    'Frecuencia de días con Precipitación superior a 0.1 mm' => array('Ene' => '15.9', 'Feb' => '12.2', 'Mar' => '9.8', 'Abr' => '2.4', 'May' => '0.3', 'Jun' => '0.1', 'Jul' => '0.0', 'Ago' => '0.4', 'Sep' => '0.9', 'Oct' => '3.5', 'Nov' => '7.4', 'Dic' => '12.7'),
#       }
# );

# Averiguar:
# ---------
# 1) Estación meteorológica más cálida del país (campo 'Temperatura máxima (°C)') y la más fria (campo: 'Temperatura mínima (°C)')
# 2) Lugar más húmedo y el más seco del país
# 3) ¿en que lugar es el mejor para poner una granja de generadores eólicos?
# 4) Temperatura promedio durante todo el año en Paraná
# 5) Agregar estación meteorológica de Libertador San Martin (inventar datos)
# 6) Sacar las estaciones que le falten algun dato (dato en null)
# 7) Mostrar todos los datos de AEROPARQUE para el mes de Abril.

ESTACION = "Estación"


def temp_mas_alta():
    temp_mas_alta = 0
    estacion = ""
    for i in estadisticas:
        for temp_max in i["Temperatura máxima (°C)"].values():
            if float(temp_max) > temp_mas_alta:
                temp_mas_alta = float(temp_max)
                estacion = i[ESTACION]
    print(
        "La estacion mas calida es: "
        + estacion
        + " con una temperatura de: "
        + str(temp_mas_alta)
        + "°C"
    )
    return estacion


def temp_mas_baja():
    temp_mas_baja = float("inf")
    estacion = ""
    for i in estadisticas:
        for temp_min in i["Temperatura mínima (°C)"].values():
            if temp_min is not None and float(temp_min) < temp_mas_baja:
                temp_mas_baja = float(temp_min)
                estacion = i[ESTACION]

    print(
        "La estacion mas fria es: "
        + estacion
        + " con una temperatura de: "
        + str(temp_mas_baja)
        + "°C"
    )
    return estacion


def lugar_mas_seco():
    humedad_alta = 0
    estacion = ""
    for i in estadisticas:
        for humedad_relativa in i["Humedad relativa (%)"].values():
            if humedad_relativa is not None and float(humedad_alta) < humedad_relativa:
                humedad_alta = float(humedad_relativa)
                estacion = i[ESTACION]
    print(
        "La estacion mas seca es: "
        + estacion
        + " con una humedad relativa de: "
        + str(humedad_alta)
        + "%"
    )
    return estacion


def lugar_menos_seco():
    humedad_baja = float("inf")
    estacion = ""
    for i in estadisticas:
        for humedad_relativa in i["Humedad relativa (%)"].values():
            if humedad_relativa is not None and float(humedad_baja) > humedad_relativa:
                humedad_baja = float(humedad_relativa)
                estacion = i[ESTACION]
    print(
        "La estacion menos seca es: "
        + estacion
        + " con una humedad relativa de: "
        + str(humedad_baja)
        + "%"
    )


def mas_viento():
    viento_promedio_max = 0
    estacion = ""
    for i in estadisticas:
        vientos = [
            viento for viento in i["Velocidad del Viento (km/h)"].values() if viento is not None]

        if len(vientos) > 0:
            promedio_viento = round(sum(vientos) / len(vientos), 2)

            if promedio_viento > viento_promedio_max:
                viento_promedio_max = promedio_viento
                estacion = i["Estación"]

    print("La estación con más viento es: " + estacion +
          " con  un promedio anual de velocidad de viento de: " + str(viento_promedio_max) + " km/h")


def temperatura_parana():
    temperatura_promedio = 0
    for i in estadisticas:
        if i[ESTACION] == "PARANÁ AERO":
            for temp in i["Temperatura (°C)"].values():
                if temp is not None:
                    temperatura_promedio += float(temp)
            temperatura_promedio = round(
                temperatura_promedio / len(i["Temperatura (°C)"]), 2
            )

    print("La temperatura promedio en Paraná es: " +
          str(temperatura_promedio) + "°C")


def generar_datos_estacion(nombre_estacion):
    datos_estacion = {
        "Estación": nombre_estacion,
        "Temperatura (°C)": {mes: float(input(f"Ingrese la temperatura promedio en °C para {nombre_estacion} en {mes}: ")) for mes in meses},
        "Temperatura máxima (°C)": {mes: float(input(f"Ingrese la temperatura máxima en °C para {nombre_estacion} en {mes}: ")) for mes in meses},
        "Temperatura mínima (°C)": {mes: float(input(f"Ingrese la temperatura mínima en °C para {nombre_estacion} en {mes}: ")) for mes in meses},
        "Humedad relativa (%)": {mes: float(input(f"Ingrese la humedad relativa en % para {nombre_estacion} en {mes}: ")) for mes in meses},
        "Velocidad del Viento (km/h)": {mes: float(input(f"Ingrese la velocidad del viento en km/h para {nombre_estacion} en {mes}: ")) for mes in meses},
        "Nubosidad total (octavos)": {mes: float(input(f"Ingrese la nubosidad total en octavos para {nombre_estacion} en {mes}: ")) for mes in meses},
        "Precipitación (mm)": {mes: float(input(f"Ingrese la precipitación en mm para {nombre_estacion} en {mes}: ")) for mes in meses},
        "Frecuencia de días con Precipitación superior a 0.1 mm": {mes: float(input(f"Ingrese la frecuencia de días con precipitación superior a 0.1 mm para {nombre_estacion} en {mes}: ")) for mes in meses},
    }
    return datos_estacion


meses = ["Ene", "Feb", "Mar", "Abr", "May", "Jun",
         "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]


def agregar_estacion(estadisticas, nombre_estacion):
    nueva_estacion = generar_datos_estacion(nombre_estacion)
    estadisticas.append(nueva_estacion)


def datos_lsm():
    temperatura_max = 0
    temperatura_min = 0
    temperatura = 0
    humedad = 0
    viento = 0
    precipitacion = 0
    nubosidad = 0
    frecuencia_precipitacion = 0
    for i in estadisticas:
        if i[ESTACION] == "LIBERTADOR SAN MARTÍN":
            for temp in i["Temperatura máxima (°C)"].values():
                if temp is not None:
                    temperatura_max += float(temp)
            temperatura_max = round(
                temperatura_max / len(i["Temperatura máxima (°C)"]), 2
            )

            for temp in i["Temperatura mínima (°C)"].values():
                if temp is not None:
                    temperatura_min += float(temp)
            temperatura_min = round(
                temperatura_min / len(i["Temperatura mínima (°C)"]))

            for temp in i["Temperatura (°C)"].values():
                if temp is not None:
                    temperatura += float(temp)
            temperatura = round(temperatura / len(i["Temperatura (°C)"]))

            for hum in i["Humedad relativa (%)"].values():
                if hum is not None:
                    humedad += float(hum)
            humedad = round(humedad / len(i["Humedad relativa (%)"]))

            for vel in i["Velocidad del Viento (km/h)"].values():
                if vel is not None:
                    viento += float(vel)
            viento = round(viento / len(i["Velocidad del Viento (km/h)"]))

            for pre in i["Precipitación (mm)"].values():
                if pre is not None:
                    precipitacion += float(pre)
            precipitacion = round(precipitacion / len(i["Precipitación (mm)"]))

            for nub in i["Nubosidad total (octavos)"].values():
                if nub is not None:
                    nubosidad += float(nub)
            nubosidad = round(nubosidad / len(i["Nubosidad total (octavos)"]))

            for frec in i[
                "Frecuencia de días con Precipitación superior a 0.1 mm"
            ].values():
                if frec is not None:
                    frecuencia_precipitacion += float(frec)
            frecuencia_precipitacion = (
                round(
                    frecuencia_precipitacion
                    / len(i["Frecuencia de días con Precipitación superior a 0.1 mm"])
                ),
                2,
            )
    print("\n")

    print("Los datos de la estación Libertador San Martín son: ")
    print(
        "La temperatura máxima promedio en Libertador San Martín es: "
        + str(temperatura_max)
        + "°C"
    )
    print(
        "La temperatura mínima promedio en Libertador San Martín es: "
        + str(temperatura_min)
        + "°C"
    )
    print(
        "La temperatura promedio en Libertador San Martín es: "
        + str(temperatura)
        + "°C"
    )
    print(
        "La humedad relativa promedio en Libertador San Martín es: "
        + str(humedad)
        + "%"
    )
    print(
        "La velocidad del viento promedio en Libertador San Martín es: "
        + str(viento)
        + "km/h"
    )
    print(
        "La precipitación promedio en Libertador San Martín es: "
        + str(precipitacion)
        + "mm"
    )
    print(
        "La nubosidad promedio en Libertador San Martín es: "
        + str(nubosidad)
        + "octavos"
    )
    print(
        "La frecuencia de días con precipitación superior a 0.1mm en Libertador San Martín es: "
        + str(frecuencia_precipitacion)
        + "%"
    )
    print("\n")


def estaciones_con_datos_faltantes():
    estaciones_faltantes = []
    for estacion in estadisticas:
        for clave in estacion:
            if clave != ESTACION:
                if any(valor is None for valor in estacion[clave].values()):
                    estaciones_faltantes.append(estacion[ESTACION])
                    break
    return estaciones_faltantes


def datos_abril_estacion(nombre_estacion):
    mes = "Abr"
    for estacion in estadisticas:
        if estacion[ESTACION] == nombre_estacion:
            print(f"Datos de {nombre_estacion} en el mes de {mes}:")
            for clave, datos in estacion.items():
                if clave != ESTACION:
                    print(f"{clave}: {datos[mes]}")


def clear_screen():
    if platform.system().lower() == "windows":
        os.system("cls")
    else:
        os.system("clear")


def menu():
    while True:
        clear_screen()
        print("Menú de opciones:")
        print("1. Estación más cálida y más fría del país")
        print("2. Lugar más húmedo y más seco del país")
        print("3. Lugar ideal para una granja de generadores eólicos")
        print("4. Temperatura promedio en Paraná durante todo el año")
        print("5. Datos de la estación Libertador San Martín")
        print("6. Estaciones con datos faltantes")
        print("7. Datos de AEROPARQUE para el mes de Abril")
        print("8. Salir")

        opcion = input("Ingrese el número de la opción que desea: ")

        if opcion == "1":
            temp_mas_alta()
            temp_mas_baja()
        elif opcion == "2":
            lugar_mas_seco()
            lugar_menos_seco()
        elif opcion == "3":
            mas_viento()
        elif opcion == "4":
            temperatura_parana()
        elif opcion == "5":
            agregar_estacion(estadisticas, "Libertador San Martin")
        elif opcion == "6":
            estaciones_faltantes = estaciones_con_datos_faltantes()
            print("Estaciones con datos faltantes:")
            for estacion in estaciones_faltantes:
                print(estacion)
        elif opcion == "7":
            nombre_estacion = "AEROPARQUE AERO"
            datos_abril_estacion(nombre_estacion)
        elif opcion == "8":
            print("Gracias por utilizar el programa. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, ingrese un número válido.")

        input("Presione ENTER para continuar...")


menu()
