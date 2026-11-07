import turtle
import os
import random
from PIL import Image, ImageTk

contador = 0

# Función para obtener la ruta correcta de los recursos
def rescource_path(relative_path):
    return os.path.join(os.path.abspath("."), relative_path)

# Configuración de la ventana
wn = turtle.Screen()

wn.title('Juego de Aeropuerto')
wn.setup(width=600, height=600)
wn.bgcolor('white')
wn.tracer(0)  # Desactiva el refresco automático para animación suave

canvas = wn.getcanvas()


# Función para crear una "imagen" en el canvas
def crear_imagen(x, y, imagen_path):
    img = Image.open(imagen_path)
    tk_img = ImageTk.PhotoImage(img)
    image_id = canvas.create_image(x, y, image=tk_img)
    return {"id": image_id, "img_ref": tk_img, "x": x, "y": y}

# Crear personajes y comida
cuerpo = crear_imagen(125, -220, rescource_path("avion.png"))
cabeza = crear_imagen(120, -280, rescource_path("player.png"))
comida = crear_imagen(-100, 80, rescource_path("aeropuerto.jpg"))

# Función para mover una imagen
def mover(imagen, dx, dy):
    imagen["x"] += dx
    imagen["y"] += dy
    canvas.coords(imagen["id"], imagen["x"], imagen["y"])

# Controles corregidos (arriba y abajo invertidos)
def arriba():
    mover(cabeza, 0, -20)
    mover(cuerpo, 0, -20)

def abajo():
    mover(cabeza, 0, 20)
    mover(cuerpo, 0, 20)

def izquierda():
    mover(cabeza, -20, 0)
    mover(cuerpo, -20, 0)

def derecha():
    mover(cabeza, 20, 0)
    mover(cuerpo, 20, 0)

# Configurar teclas
wn.listen()
wn.onkeypress(arriba, "Up")
wn.onkeypress(abajo, "Down")
wn.onkeypress(izquierda, "Left")
wn.onkeypress(derecha, "Right")

# Lista de imágenes del cuerpo
cuerpos = [
    rescource_path("avion1.png"),
    rescource_path("avion2.png"),
    rescource_path("avion3.png"),
    rescource_path("avion4.png"),
]


# Función para actualizar el cuerpo de manera suave
def actualizar_cuerpo():
    global cuerpo
    if contador < 3:
        img_path = cuerpos[0]
    elif contador < 5:
        img_path = cuerpos[1]
    elif contador < 7:
        img_path = cuerpos[2]
    else:
        img_path = cuerpos[3]

    img = Image.open(img_path)
    tk_img = ImageTk.PhotoImage(img)
    canvas.itemconfig(cuerpo["id"], image=tk_img)
    cuerpo["img_ref"] = tk_img  # Mantener referencia

# Bucle principal del juego
def game_loop():
    global contador

    # Colisión cabeza-comida
    if abs(cabeza["x"] - comida["x"]) < 20 and abs(cabeza["y"] - comida["y"]) < 20:
        comida["x"] = random.randint(-260, 260)
        comida["y"] = random.randint(-260, 260)
        canvas.coords(comida["id"], comida["x"], comida["y"])
        contador += 1
        actualizar_cuerpo()

    
    wn.update()  # Refresca la pantalla
    wn.ontimer(game_loop, 100)  # Repite cada 100ms


# Iniciar juego
game_loop()
wn.mainloop()
#Final del codigo
