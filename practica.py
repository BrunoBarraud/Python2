import random

# Historias Locas

# Concatenar cadenas de caracteres

# Aprende a programar con _________

# organizacion = "TuVieja.net"

# print("Aprende a programar con " + organizacion) 
# print ("Aprende a programar con {}".format(organizacion))
# print (f"Aprende a programar con {organizacion}") #f-string

# adj = input("Adjetivo: ")
# sustantivo_comun = input("Sustantivo común: ")

# madlib = f"¡Programar es tan {adj}! Siempre me emociona porque me encanta {sustantivo_comun}."

# print(madlib)

#Adivina el numero pajin 2.0

# def advina_el_numero(x):
#     print("=====================================")
#     print("Bienvenido pajin!")
#     print("=====================================")
#     print("Tu goal es adivinar el numero generado por la pinche computadora del ojete. ")
#     print("Si adivinas, ganas. Si no, pierdes xd obviamente no vas a ganar. ")

#     numero_secreto = random.randint(1, x)

#     prediction = 0


#     while prediction != numero_secreto:
#         prediction = int(input(f"Adivina un numero del 1 al {x}: "))
#         if prediction < numero_secreto:
#             print("No mames, es mas grande que eso")
#         elif prediction > numero_secreto:
#             print("No mames, es mas chico que eso")
        
#     print(f"¡Adivinaste pajin a remo! El numero era {numero_secreto}")


# advina_el_numero(1000)

#La pc es re crack y te adivina el numero que estes pensando

# def adivina_el_numero_computadora(x):


#     print("=====================================")
#     print("Bienvenido pajin!")
#     print("=====================================")
#     print(f"Piensa un numero del 1 a {x} y yo lo adivino. ")

#     limite_inferior = 1
#     limite_superior = x

#     feedback = ""

#     while feedback != "c":
#         if limite_inferior != limite_superior:
#             prediction = random.randint(limite_inferior, limite_superior)
#         else:
#             prediction = limite_inferior
#         feedback = input(f"¿El numero {prediction} es muy alto (A), muy bajo (B) o correcto (C)? ").lower()
#         if feedback == "a":
#             limite_superior = prediction - 1
#         elif feedback == "b":
#             limite_inferior = prediction + 1

#     print(f"¡Adivine pajin! algo mas dificil no tenes pa? El numero era {prediction}")


# adivina_el_numero_computadora(500)

#El juegito de piedra, papel o tijera wacho

# def juego_ppt():
#     usuario = input("¿Piedra (P), Papel (A) o Tijera (T)? ").lower()
#     computadora = random.choice(["p", "a", "t"])

#     if usuario == computadora:
#         return "Empate"

#     if gana_el_jugador(usuario, computadora):
#         return "Ganaste pajin"


#     return "Perdiste pajin"


# def gana_el_jugador(jugador, oponente):
#     # return true si gana el jugador
#     # p > t, t > a, a > p
#     if ((jugador == "pi" and oponente == "ti") or (jugador == "ti" and oponente == "pa") or (jugador == "pa" and oponente == "pi")):
#         return True
#     else:
#         return False
    

# print(juego_ppt())

# Juego del ahorcado

from palabras import palabras
from ahorcado_diagramos import vidas_diccionario_visual
import string

def obtener_palabra_secreta(palabras):
    palabra = random.choice(palabras)

    while "-" in palabra or " " in palabra:
        palabra = random.choice(palabras)

    return palabra.upper()



def ahorcado():
    print ("=====================================")
    print ("Bienvenido al juego del ahorcado")
    print ("=====================================")

    palabra = obtener_palabra_secreta(palabras)
    
    letras_por_adivinar = set(palabra)
    letras_adivinadas = set()
    abecedario = set(string.ascii_uppercase)
    intentos = 7

    while len(letras_por_adivinar) > 0 and intentos > 0:
        print(f"Te quedan {intentos} intentos y has usado estas letras: {' '.join(letras_adivinadas)}")

        #mostrar el estado actual de la plabra
        palabra_lista = [letra if letra in letras_adivinadas else "-" for letra in palabra]
        print(vidas_diccionario_visual[intentos])
        print(f"Palabra: {' '.join(palabra_lista)}")

        letra_usuario = input("Adivina una letra: ").upper()

        if letra_usuario in abecedario - letras_adivinadas:
            letras_adivinadas.add(letra_usuario)
            if letra_usuario in letras_por_adivinar:
                letras_por_adivinar.remove(letra_usuario)
                print("")
            else:
                intentos = intentos - 1
                print(f"La letra {letra_usuario} no esta en la palabra.")
                