import os
import random
import messagebox
import tkinter
from tkinter import *
import tkintermapview
from PIL import Image, ImageTk

def dijkstra(Grafo, inicio, final):
    dist, prev = {}, {}
    result = []

    for vertice in Grafo:
        dist[vertice] = float("inf")
        prev[vertice] = None
        dist[inicio] = 0

    Q = [vertice for vertice in Grafo]

    while Q:
        u = min(Q, key=dist.get)
        Q.remove(u)
        result.append(u)

        for vecino in Grafo[u]:
            if vecino in Q and dist[vecino] > dist[u] + Grafo[u][vecino]:
                dist[vecino] = dist[u] + Grafo[u][vecino]
                prev[vecino] = u

    recorrido = []
    actual = final
    while actual is not None:
        recorrido.insert(0, actual)
        actual = prev[actual]

    return result, dist, recorrido
    
def aleatorio():
    return random.randint(1, 80)

def obtener_datos():
    origen = entry_origen.get()
    destino = entry_destino.get()

    if origen not in grafo or destino not in grafo:
         messagebox.showwarning("Advertencia", "Por favor, ingrese ruta correcta.")
    elif origen and destino:
        s, distancia, recorrido = dijkstra(grafo, origen, destino)
        print(f"{s=}")
        print(f"{distancia=}")
        print(f"{recorrido=}")
        print(grafo)
        crear_mapa(recorrido)

    else:
        messagebox.showwarning("Advertencia", "Por favor, completa ambos campos.")

def create_custom_marker(map_view, lat, lon, text):
    marker = Canvas(map_view, width=100, height=50, bd=0, highlightthickness=0)
    marker.create_text(50, 25, text=text, font=("Arial", 14), fill="black")
    map_view.set_marker(lat, lon, text=text)

def crear_mapa(trayectoria):
    # load images
    current_path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
    plane_image = ImageTk.PhotoImage(Image.open(os.path.join(current_path, "images", "images.png")).resize((1, 1)))

    # create map widget
    map_widget = tkintermapview.TkinterMapView(root_tk, width=800, height=600, corner_radius=0)
    map_widget.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    map_widget.set_position(7.1177284, -73.1163292)

    # set current widget position by address
    data_path = []
    for ruta in trayectoria:
        marker = map_widget.set_position(coordenadas[ruta][0], coordenadas[ruta][1], marker=True, )
        marker.set_text(ruta)
        data_path.append(marker.position)
        
    path_1 = map_widget.set_path(data_path)



""" grafo = {
    'a': {'b': aleatorio(), 'f': aleatorio()},
    'b': {'d': aleatorio()},
    'c': {'a': aleatorio(), 'f': aleatorio()},
    'd': {'h': aleatorio(), 'e': aleatorio()},
    'e': {'a': aleatorio()},
    'f': {'l': aleatorio(), 'c': aleatorio()},
    'g': {'c': aleatorio(), 'm': aleatorio()},
    'h': {'n': aleatorio()},
    'i': {'h': aleatorio(), 'ñ': aleatorio()},
    'j': {'d': aleatorio(), 'i': aleatorio()},
    'k': {'e': aleatorio(), 'j': aleatorio(), 'l': aleatorio()},
    'l': {'k': aleatorio(), 'q': aleatorio(),'m': aleatorio()},
    'm': {'l': aleatorio(), 'g': aleatorio(), 'r': aleatorio()},
    'n': {'t': aleatorio()},
    'ñ': {'n': aleatorio(), 'i':aleatorio(), 'u': aleatorio()},
    'o': {'ñ': aleatorio(), 'j': aleatorio()},
    'p': {'o': aleatorio(), 'k': aleatorio()},
    'q': {'x': aleatorio(), 'p': aleatorio()},
    'r': {'z': aleatorio(), 'q': aleatorio()},
    's': {'g': aleatorio(), 'r': aleatorio()},
    't': {'u': aleatorio()},
    'u': {'v': aleatorio(), 'ñ': aleatorio()},
    'v': {'o': aleatorio(), 'w': aleatorio()},
    'w': {'p': aleatorio(), 'x': aleatorio()},
    'x': {'y': aleatorio()},
    'y': {'z': aleatorio(), 'z3': aleatorio()},
    'z': {'z1': aleatorio()},
    'z1': {'z2': aleatorio(), 'z3': aleatorio()},
    'z2': {'s': aleatorio()},
    'z3': {'z4': aleatorio()},
    'z4': {'z5': aleatorio()},
    'z5': {'z2': aleatorio()}
} """

grafo = {
    'a': {'b': 3, 'f': 3 },
    'b': {'d': 5},
    'c': {'a': 4, 'f': 3},
    'd': {'h': 2, 'e': 4},
    'e': {'a': 1},
    'f': {'l': 6, 'c': 3},
    'g': {'c': 2, 'm': 3},
    'h': {'n': 8},
    'i': {'h': 1, 'ñ': 2},
    'j': {'d': 5, 'i': 3},
    'k': {'e': 3, 'l': 4, 'j': 1},
    'l': {'k': 4, 'q': 2,'m': 3},
    'm': {'l': 3, 'g': 3, 'r': 2},
    'n': {'t': 2},
    'ñ': {'n': 2, 'i': 2, 'u': 5},
    'o': {'ñ': 2, 'j': 1},
    'p': {'o': 3, 'k': 2},
    'q': {'x': 1, 'p': 3},
    'r': {'z': 3, 'q': 2},
    's': {'g': 1, 'r': 1},
    't': {'u': 3},
    'u': {'v': 4, 'ñ': 5},
    'v': {'o': 3, 'w': 1},
    'w': {'p': 3, 'x': 11},
    'x': {'y': 2},
    'y': {'z': 2, 'z3': 3},
    'z': {'z1': 3},
    'z1': {'z2': 3, 'z3': 1},
    'z2': {'s': 1},
    'z3': {'z4': 1},
    'z4': {'z5': 1},
    'z5': {'z2': 3}
}

coordenadas = {
    'a' : [7.1171264, -73.1182106],
    'b' : [7.1174032, -73.1182348],
    'c' : [7.1165195,-73.1175857],
    'd' : [7.1179088, -73.1179827],
    'e' : [7.1172115, -73.1177574],
    'f' : [7.1169507, -73.1174194],
    'g' : [7.1160138, -73.1171029],
    'h' : [7.1189360, -73.1172802],
    'i' : [7.1185208, -73.1170871],
    'j' : [7.1178978, -73.1168082],
    'k' : [7.1174826, -73.1166526],
    'l' : [7.1168918, -73.1166526],
    'm' : [7.1164074, -73.1168135],
    'n' : [7.1193082, -73.1166340],
    'ñ' : [7.1188611, -73.1164141],
    'o' : [7.1183767, -73.1161995],
    'p' : [7.1176208, -73.1161244],
    'q' : [7.1168164, -73.1159796],
    'r' : [7.1160214, -73.1160815],
    's' : [7.1154412, -73.1165321],
    't' : [7.1197470, -73.1160171],
    'u' : [7.1192147, -73.1157596],
    'v' : [7.1187675, -73.1156255],
    'w' : [7.1177828, -73.1154807],
    'x' : [7.1167490, -73.1153455],
    'y' : [7.1157642, -73.1152382],
    'z' : [7.1156311, -73.1153067],
    'z1' : [7.1152106, -73.1155642],
    'z2' : [7.1147741, -73.1159397],
    'z3' : [7.1148593, -73.1151189],
    'z4' : [7.1144068, -73.1150405],
    'z5' : [7.1141513, -73.1152980]
}

# create tkinter window
root_tk = tkinter.Tk()
root_tk.geometry(f"{800}x{600}")
root_tk.title("map_view_example.py")

# Crear dos campos de entrada
label_origen = tkinter.Label(root_tk, text="Origen:")
label_origen.grid(row=0, column=0, padx=10, pady=10)
entry_origen = tkinter.Entry(root_tk)
entry_origen.grid(row=0, column=1, padx=10, pady=10)

label_destino = tkinter.Label(root_tk, text="Destino:")
label_destino.grid(row=1, column=0, padx=10, pady=10)
entry_destino = tkinter.Entry(root_tk)
entry_destino.grid(row=1, column=1, padx=10, pady=10)

# Crear un botón para ejecutar la función dijkstra
boton_ejecutar = tkinter.Button(root_tk, text="Ejecutar Dijkstra", command=obtener_datos)
boton_ejecutar.grid(row=2, column=0, columnspan=2, pady=10)

# Cargar imagen del disco.
current_path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
fondo_inicio = ImageTk.PhotoImage(Image.open(os.path.join(current_path, "images", "fondo.png")).resize((300, 400)))
label = tkinter.Label(root_tk, image=fondo_inicio)
label.grid(row=3, column=3, padx=70, pady=10)

root_tk.mainloop()