import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

cliente = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Lista que guarda el historial de la conversación
historial = []

def preguntar(pregunta):
    historial.append(f"Usuario: {pregunta}")
    
    contexto_completo = "\n".join(historial)
    
    respuesta = cliente.models.generate_content(
        model="gemini-2.5-flash",
        contents=contexto_completo
    )
    
    historial.append(f"Asistente: {respuesta.text}")
    return respuesta.text

# Prueba con dos preguntas relacionadas
print(preguntar("Me llamo Paul y estoy aprendiendo Python"))
print("---")
print(preguntar("¿Cuál es mi nombre y qué estoy aprendiendo?"))
print("---")
print(preguntar("Porque python es bueno?"))
