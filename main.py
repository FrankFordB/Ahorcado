# -*- coding: utf-8 -*-
"""

TP de Ahorcado
Franco Burgoa

"""
import random
import os
import time
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def inicio(request: Request):
    return templates.TemplateResponse(request, "index.html")

################################ FUNCIONES ####################################

def list_to_string(palabra):
    texto=""
    for letra in palabra:
        texto= texto + letra
    return texto

def list_to_oculta(oculta):
    texto=""
    for letra in oculta:
        texto= texto+" "+ letra
    return texto

listaPalabras = ["python","computadora","teclado","monitor","raton",
                 "programa","variable","funcion","bucle","condicion",
                 "internet","servidor","archivo","carpeta","memoria",
                 "pantalla","codigo","juego","ahorcado","musica",
                 "guitarra","piano","bateria","sintesis","cancion",
                 "ritmo","melodia","escuela","cuaderno","lapiz",
                 "mochila","profesor","alumno","examen","matematica",
                 "historia","geografia","biologia","futbol","pelota",
                 "arquero","cancha","golazo","camiseta","entrenador",
                 "montana","rio","bosque","desierto","planeta",
                 "estrella","galaxia","luna","sol","tormenta"]

if __name__ == "__main__":
    palabra=list(random.choice(listaPalabras))
    oculta=list("_"*len(palabra))

    respuesta=0
    letra=0
    contador_medio=7
    contador_facil=10
    contador_dificil=3

    print(" _______________________________________________________________________")
    print("├                                                                      ┤")
    print("├                    🎮 Bienvenido a EndGames 🎮                      ┤")
    print("├                     🔎 Juego del Ahorcado 🔎                        ┤")
    print("├______________________________________________________________________┤")

    dificultad= int(input("\n"
    "---------------- Elija la dificultad y presione Enter ------------------\n"
    "\n1= Facilito 🗿 (10 intentos)"
    "\n2= Masomeno 🫦 (7 intentos)"
    "\n3= Dificil  🔥 (3 Intentos)\nIngrese el nivel: "))

    print(palabra)

    # ========================= FACIL =========================

    if dificultad==1:
        print("")
        print("Palabra            :", list_to_oculta(oculta),)
        print(f"\nCantidad de intentos restantes {contador_facil}")

        while (palabra!=oculta) and (contador_facil>=1):

            letra=input("Ingrese una letra: ")

            if letra.isalpha() and len(letra)==1 and letra in palabra:

                for i in range(len(palabra)):
                    if palabra[i]==letra:
                        oculta[i]=letra

                print("\n========================================")
                print("Intentos restantes :", contador_facil)
                print("Letra ingresada    :", letra)
                print("Estado             : CORRECTO")
                print("Palabra            :", list_to_oculta(oculta))
                print("========================================")
                
                if palabra==oculta:
                    print("Ganaste Crack")
            elif not letra.isalpha() or len(letra) > 1:
                print("\nIngrese solo una letra válida\n")
            else:

                contador_facil-=1

                print("\n========================================")
                print("Intentos restantes :", contador_facil)
                print("Letra ingresada    :", letra)
                print("Estado             : INCORRECTO")
                print("Palabra            :", list_to_oculta(oculta))
                print("========================================")
                print("Tu letra no esta.")
                
            if contador_facil==0:
                print("PERDISTE, SOS EL PIOR")


    # ========================= MEDIO =========================

    if dificultad==2:
        print("Palabra            :", list_to_oculta(oculta))
        print(f"\nCantidad de intentos restantes {contador_medio}")

        while (palabra!=oculta) and (contador_medio>=1):

            letra=input("Ingrese una letra: ")

            if letra.isalpha() and len(letra)==1 and letra in palabra:

                for i in range(len(palabra)):
                    if palabra[i]==letra:
                        oculta[i]=letra

                print("\n========================================")
                print("Intentos restantes :", contador_medio)
                print("Letra ingresada    :", letra)
                print("Estado             : CORRECTO")
                print("Palabra            :", list_to_oculta(oculta))
                print("========================================")

                if palabra==oculta:
                    print("Ganaste Crack")
            elif not letra.isalpha() or len(letra) > 1:
                print("\nIngrese solo una letra válida\n")
            else:

                contador_medio-=1

                print("\n========================================")
                print("Intentos restantes :", contador_medio)
                print("Letra ingresada    :", letra)
                print("Estado             : INCORRECTO")
                print("Palabra            :", list_to_oculta(oculta))
                print("========================================")
                print("Tu letra no esta.")

            if contador_medio==0:
                print("PERDISTE, SOS EL PIOR")


    # ========================= DIFICIL =========================

    if dificultad==3:
        print("Palabra            :", list_to_oculta(oculta))
        print(f"\nCantidad de intentos restantes {contador_dificil}")

        while (palabra!=oculta) and (contador_dificil>=1):

            letra=input("Ingrese una letra: ")

            if letra.isalpha() and len(letra)==1 and letra in palabra:

                for i in range(len(palabra)):
                    if palabra[i]==letra:
                        oculta[i]=letra
            
                print("\n========================================")
                print("Intentos restantes :", contador_dificil)
                print("Letra ingresada    :", letra)
                print("Estado             : CORRECTO")
                print("Palabra            :", list_to_oculta(oculta))
                print("========================================")

                if palabra==oculta:
                    print("Ganaste Crack")
            elif not letra.isalpha() or len(letra) > 1:
                print("\nIngrese solo una letra válida\n")
                
            else:

                contador_dificil-=1

                print("\n========================================")
                print("Intentos restantes :", contador_dificil)
                print("Letra ingresada    :", letra)
                print("Estado             : INCORRECTO")
                print("Palabra            :", list_to_oculta(oculta))
                print("========================================")
                print("Tu letra no esta.")

            if contador_dificil==0:
                print("PERDISTE, SOS EL PIOR")