from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

TOKEN = "8623974595:AAHCOVd0ZxRiJrup3Ytw1nnMHWxSAzksSfQ"

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Сообщение получено!")

app = Application.builder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.TEXT, handle_message))

app.run_polling()
