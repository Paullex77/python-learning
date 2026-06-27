import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

cliente = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

pregunta = input("Escribe tu pregunta para la IA: ")

respuesta = cliente.models.generate_content(
    model="gemini-2.5-flash",
    contents=pregunta
)

print("\nRespuesta:")
print(respuesta.text)