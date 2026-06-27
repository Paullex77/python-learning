import os
import sqlite3
from dotenv import load_dotenv
from google import genai

load_dotenv()
cliente = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

conexion = sqlite3.connect("conversaciones.db")
cursor = conexion.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS mensajes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    rol TEXT NOT NULL,
    contenido TEXT NOT NULL
)
""")
conexion.commit()

def guardar_mensaje(rol, contenido):
    cursor.execute("INSERT INTO mensajes (rol, contenido) VALUES (?, ?)", (rol, contenido))
    conexion.commit()

def cargar_historial():
    cursor.execute("SELECT rol, contenido FROM mensajes ORDER BY id")
    filas = cursor.fetchall()
    return [f"{rol}: {contenido}" for rol, contenido in filas]

def preguntar(pregunta):
    guardar_mensaje("Usuario", pregunta)
    
    historial = cargar_historial()
    contexto_completo = "\n".join(historial)
    
    respuesta = cliente.models.generate_content(
        model="gemini-2.5-flash",
        contents=contexto_completo
    )
    
    guardar_mensaje("Asistente", respuesta.text)
    return respuesta.text

print(preguntar("Hola, soy Paul y me gusta el futbol"))
print("---")
print(preguntar("¿Cuál es mi nombre?"))
print("---")
print(preguntar("¿Cuál es mi deporte favorito?"))