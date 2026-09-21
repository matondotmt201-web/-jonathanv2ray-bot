import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Salut Boss ! Ton bot VPN est en ligne 🚀\nEnvoie /v2ray pour une config.")

async def v2ray(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Config V2Ray : vmess://exemple-a-changer")

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("v2ray", v2ray))
app.run_polling()
