import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters
from google import genai

load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")
cliente = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hola, soy tu bot con IA. Escríbeme cualquier pregunta.")

from datetime import datetime

async def responder_con_ia(update: Update, context: ContextTypes.DEFAULT_TYPE):
    pregunta = update.message.text
    usuario = update.message.from_user.first_name
    print(f"{usuario} preguntó: {pregunta}")
    
    fecha_actual = datetime.now().strftime("%Y-%m-%d")
    contexto = f"La fecha de hoy es {fecha_actual}. Pregunta del usuario: {pregunta}"
    
    respuesta = cliente.models.generate_content(
        model="gemini-2.5-flash",
        contents=contexto
    )
    
    await update.message.reply_text(respuesta.text)

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, responder_con_ia))

print("Bot iniciado. Presiona Ctrl+C para detenerlo.")
app.run_polling()