
import requests 

respuesta = requests.get("http://api.github.com/users/torvalds")
datos = respuesta.json()

print("Status code:", respuesta.status_code)
print("Nombre:", datos["name"])
print("Bio:", datos["bio"])
print("Repos publicos:", datos["public_repos"])
print("Seguidores:", datos["followers"])

import requests
latitud = -0.1807
longitud = -78.4678

url = f"https://api.open-meteo.com/v1/forecast?latitude={latitud}&longitude={longitud}&current_weather=true"

respuesta = requests.get(url)
datos = respuesta.json()
clima_actual = datos["current_weather"]
print(f"Temperatura: {clima_actual['temperature']}°C")
print(f"Velocida del viento: {clima_actual['windspeed']} km/h" )
print(f"Hora del reporte: {clima_actual['time']}")

if clima_actual["temperature"] > 20:
    print ("Hace calor")
elif clima_actual["temperature"] > 10:
    print ("Clima templado")
else:
    print("Hace frio")

