import os
import sqlite3
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters
from google import genai
from datetime import datetime

load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")
cliente = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Base de datos para guardar conversaciones por usuario
conexion = sqlite3.connect("bot_telegram.db", check_same_thread=False)
cursor = conexion.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS mensajes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    chat_id INTEGER NOT NULL,
    rol TEXT NOT NULL,
    contenido TEXT NOT NULL
)
""")
conexion.commit()

def guardar_mensaje(chat_id, rol, contenido):
    cursor.execute("INSERT INTO mensajes (chat_id, rol, contenido) VALUES (?, ?, ?)",
                   (chat_id, rol, contenido))
    conexion.commit()

def cargar_historial(chat_id):
    cursor.execute("SELECT rol, contenido FROM mensajes WHERE chat_id = ? ORDER BY id",
                   (chat_id,))
    filas = cursor.fetchall()
    return [f"{rol}: {contenido}" for rol, contenido in filas]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hola, soy tu bot con memoria. Escríbeme lo que quieras.")

async def responder_con_ia(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.message.chat_id
    pregunta = update.message.text
    usuario = update.message.from_user.first_name
    
    print(f"{usuario} (chat_id {chat_id}) preguntó: {pregunta}")
    
    guardar_mensaje(chat_id, "Usuario", pregunta)
    historial = cargar_historial(chat_id)
    contexto_completo = "\n".join(historial)
    
    respuesta = cliente.models.generate_content(
        model="gemini-2.5-flash",
        contents=contexto_completo
    )
    
    guardar_mensaje(chat_id, "Asistente", respuesta.text)
    await update.message.reply_text(respuesta.text)

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, responder_con_ia))

print("Bot iniciado. Presiona Ctrl+C para detenerlo.")
app.run_polling()                                