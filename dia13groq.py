import os
import sqlite3
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters
from groq import Groq

load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")
cliente_groq = Groq(api_key=os.getenv("GROQ_API_KEY"))

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
    return filas

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hola, soy tu bot con memoria (ahora con Groq). Escríbeme lo que quieras.")

async def responder_con_ia(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.message.chat_id
    pregunta = update.message.text
    usuario = update.message.from_user.first_name
    
    print(f"{usuario} (chat_id {chat_id}) preguntó: {pregunta}")
    
    guardar_mensaje(chat_id, "Usuario", pregunta)
    historial = cargar_historial(chat_id)
    
    mensajes_formato_groq = []
    for rol, contenido in historial:
        rol_groq = "user" if rol == "Usuario" else "assistant"
        mensajes_formato_groq.append({"role": rol_groq, "content": contenido})
    
    respuesta = cliente_groq.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=mensajes_formato_groq
    )
    
    texto_respuesta = respuesta.choices[0].message.content
    
    guardar_mensaje(chat_id, "Asistente", texto_respuesta)
    await update.message.reply_text(texto_respuesta)

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, responder_con_ia))

print("Bot iniciado con Groq. Presiona Ctrl+C para detenerlo.")
app.run_polling()