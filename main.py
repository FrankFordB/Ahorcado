import random
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

listaPalabras = ["computadora",
    "teclado",
    "monitor",
    "raton",
    "programacion",
    "algoritmo",
    "variable",
    "funcion",
    "bucle",
    "condicion",
    "python",
    "javascript",
    "servidor",
    "internet",
    "archivo",
    "carpeta",
    "pantalla",
    "codigo",
    "sistema",
    "memoria",
    "procesador",
    "compilador",
    "depuracion",
    "software",
    "hardware",
    "desarrollo",
    "frontend",
    "backend",
    "framework",
    "biblioteca",
    "musica",
    "guitarra",
    "piano",
    "bateria",
    "melodia",
    "ritmo",
    "cancion",
    "concierto",
    "partitura",
    "instrumento",
    "escuela",
    "profesor",
    "alumno",
    "cuaderno",
    "lapiz",
    "examen",
    "matematica",
    "historia",
    "geografia",
    "biologia",
    "fisica",
    "quimica",
    "universidad",
    "biblioteca",
    "futbol",
    "pelota",
    "arquero",
    "cancha",
    "camiseta",
    "entrenador",
    "golazo",
    "torneo",
    "campeonato",
    "seleccion",
    "montana",
    "desierto",
    "bosque",
    "planeta",
    "galaxia",
    "estrella",
    "tormenta",
    "oceano",
    "volcan",
    "naturaleza",
    "aventura",
    "bicicleta",
    "automovil",
    "carretera",
    "semáforo",
    "ciudad",
    "edificio",
    "ventana",
    "puerta",
    "escalera",
    "telefono",
    "mensaje",
    "aplicacion",
    "navegador",
    "contraseña",
    "seguridad",
    "robotica",
    "inteligencia",
    "artificial",
    "aprendizaje",
    "datos",
    "estadistica",
    "conexion",
    "digital",
    "tecnologia",
    "innovacion"]

# Estado global del juego
juego = {
    "palabra": [],
    "oculta": [],
    "intentos": 7,
    "letras_usadas": [],
    "letras_usadas_mal": [],
    "mensaje": "",
    "terminado": False,
    "color_letra": "green",
    "color_letra_mal": "red"
}

def nuevo_juego():
    palabra = list(random.choice(listaPalabras))
    juego["palabra"] = palabra
    juego["oculta"] = ["_"] * len(palabra)
    juego["intentos"] = 7
    juego["letras_usadas"] = []
    juego["letras_usadas_mal"] = []
    juego["mensaje"] = "Buena suerte"
    juego["terminado"] = False
    juego["color_letra"] = "white"

def get_contexto(request):
    return {
        "oculta": " ".join(juego["oculta"]),
        "intentos": juego["intentos"],
        "letras_usadas":  "  ".join(juego["letras_usadas"])  ,
        "letras_usadas_mal":"  ".join(juego["letras_usadas_mal"]),
        "mensaje": juego["mensaje"],
        "terminado": juego["terminado"],
        "mostrar_modal": "flex" if juego["terminado"] else "none",  
        "DEBUG": True,
        "color_letra": juego["color_letra"],
        "color_letra_mal":juego["color_letra_mal"],
        
    }


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    nuevo_juego()
    return templates.TemplateResponse(request=request, name="index.html", context=get_contexto(request))

@app.get("/wikipedia")
def wikipedia(request: Request):
    return templates.TemplateResponse(request=request, name="wikipedia.html", context={})

@app.post("/", response_class=HTMLResponse)
def enviar(request: Request, letra: str = Form(...)):
    letra = letra.lower()

    if juego["terminado"]:
        juego["mensaje"] = "El juego terminó. Iniciá una nueva partida."

    elif not letra.isalpha() or len(letra) != 1:
        juego["mensaje"] = "Ingresá solo una letra válida."

    elif letra in juego["letras_usadas"] :
        juego["mensaje"] = f"Ya usaste la letra '{letra}'."

    elif letra in juego["letras_usadas_mal"] :
        juego["mensaje"] = f"Ya usaste la letra '{letra}'."
    
    elif letra in juego["palabra"]:
        juego["letras_usadas"].append(letra)
        for i, l in enumerate(juego["palabra"]):
            if l == letra:
                juego["oculta"][i] = letra
        juego["mensaje"] = f"¡Correcto! '{letra}' está en la palabra."
        juego["color_letra"]= "green"

        if juego["oculta"] == juego["palabra"]:
            juego["mensaje"] = "¡GANASTE!"
            juego["terminado"] = True
    else:
        juego["letras_usadas_mal"].append(letra)
        juego["intentos"] -= 1
        juego["mensaje"] = f"'{letra}' no está en la palabra."
        juego["color_letra_mal"]= "red"

        if juego["intentos"] == 0:
            juego["mensaje"] = f"PERDISTE!! La palabra era: {''.join(juego['palabra'])}"
            juego["terminado"] = True

    return templates.TemplateResponse(request=request, name="index.html", context=get_contexto(request))