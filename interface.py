import folium
import random
import webview
import os
from threading import Thread
from time import sleep

# variável global para coordenadas do drone
drone_lat, drone_lon, drone_alt = 0.0, 0.0, 10.0

def create_map(lat, lon, alt):
    drone_map = folium.Map(location=[lat, lon], zoom_start=15)
    drone_icon = folium.CustomIcon("drone.gif", icon_size=(50, 50))
    folium.Marker([lat, lon], icon=drone_icon, popup=f"Drone (Alt: {alt}m)").add_to(drone_map)
    map_file = "drone_map.html"
    drone_map.save(map_file)
    return map_file

def update_coordinates(direction):
    global drone_lat, drone_lon
    step = 0.001
    if direction == "up":
        drone_lat += step
    elif direction == "down":
        drone_lat -= step
    elif direction == "left":
        drone_lon -= step
    elif direction == "right":
        drone_lon += step
    create_map(drone_lat, drone_lon, drone_alt)

def update_altitude(new_altitude):
    global drone_alt
    drone_alt = new_altitude
    create_map(drone_lat, drone_lon, drone_alt)

def take_off():
    print("Drone está levantando voo!")

def irrigate():
    print("Drone está irrigando!")

def update_map(window):
    global drone_lat, drone_lon, drone_alt
    while True:
        create_map(drone_lat, drone_lon, drone_alt)
        window.load_url(os.path.abspath("drone_map.html"))
        sleep(2)

if __name__ == "__main__":
    drone_lat, drone_lon, drone_alt = random.uniform(-90.0, 90.0), random.uniform(-180.0, 180.0), 10.0
    create_map(drone_lat, drone_lon, drone_alt)

    window = webview.create_window("Drone Interface com Mapa", os.path.abspath("drone_map.html"))

    window.expose(update_coordinates)
    window.expose(update_altitude)
    window.expose(take_off)
    window.expose(irrigate)

    Thread(target=update_map, args=(window,), daemon=True).start()

    html_controls = """
    <html>
    <head>
        <style>
            body { font-family: Arial, sans-serif; text-align: center; margin-top: 20px; }
            button { margin: 5px; padding: 10px; font-size: 16px; }
            input { padding: 10px; font-size: 16px; margin-top: 10px; }
        </style>
    </head>
    <body>
        <h3>Controles do Drone</h3>
        <button onclick="pywebview.api.update_coordinates('up')">Frente</button><br>
        <button onclick="pywebview.api.update_coordinates('left')">Esquerda</button>
        <button onclick="pywebview.api.update_coordinates('right')">Direita</button><br>
        <button onclick="pywebview.api.update_coordinates('down')">Trás</button><br><br>
        <button onclick="pywebview.api.take_off()">Levantar Voo</button><br><br>
        <button onclick="pywebview.api.irrigate()">Irrigar</button><br><br>
        <label for="altitude">Altura (m):</label>
        <input type="number" id="altitude" name="altitude" value="10" min="0" step="1" 
               onchange="pywebview.api.update_altitude(parseFloat(this.value))"><br><br>
    </body>
    </html>
    """

    controls_window = webview.create_window("Controles do Drone", html=html_controls)

    webview.start()
