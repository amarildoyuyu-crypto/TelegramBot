
import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

# Configurar registos para ver o que se passa
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Olá! O meu bot de monitorização está online e a funcionar 24 horas.")

def main():
    # O token do seu bot do Telegram deve ser configurado nas variáveis de ambiente do Render
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    if not token:
        print("Erro: TELEGRAM_BOT_TOKEN não encontrado nas variáveis de ambiente.")
        return

    application = ApplicationBuilder().token(token).build()

    # Comando /start
    application.add_handler(CommandHandler("start", start))

    # Iniciar o bot
    print("Bot a iniciar...")
    application.run_polling()

if __name__ == '__main__':
    main()
