import os
import threading
from flask import Flask
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# --- PARTIE WEB POUR RENDER ---
app = Flask(__name__)
@app.route('/')
def home():
    return "Bot IR MISSI est en ligne!"

def run_web():
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

threading.Thread(target=run_web, daemon=True).start()

# --- CONFIGURATION ---
BOT_TOKEN = os.environ.get("BOT_TOKEN")
ADMIN_ID = int(os.environ.get("ADMIN_ID", "123456789"))
SITE_WEB = "https://ir-missi-espoir.netlify.app"
WHATSAPP = "https://wa.me/243972104149"

# Tes configs
VMESS_CONFIG = "vmess://eyJhZGQiOiJ1cy0yMy5oaWh1Lm5ldCIsImFpZCI6IjAiLCJpZCI6IjM4ZTgxNjEwLWIwZDEtMTFmMS1iNzM5LTIwNWM2ZDVmNWQ3OCIsImhvc3QiOiJhaXJ0ZWxjYXJlYXBwLmFpcnRlbC5jZC51cy0yMy5oaWh1Lm5ldCIsIm5ldCI6IndzIiwicGF0aCI6Ii9lczh3ZzJuMyIsInBvcnQiOiI4MCIsInBzIjoiVm1lc3MgVVNBIFZpcmdpbmlhIDIwMjYtMDktMjIiLCJ0bHMiOiIiLCJ0eXBlIjoibm9uZSIsInYiOiIyIn0="
VLESS_CONFIG = "vless://I_Love_🇵🇸_sshOcean_56e2@airtelcareapp.airtel.cd.us-23.hihu.net.fr1.v2less.online:443?encryption=none&security=tls&sni=fr1.v2less.online&type=grpc&serviceName=vless-grpc&mode=gun#MISS🤖"

# Clavier principal
KEYBOARD = [
    [InlineKeyboardButton("🚀 Obtenir VMESS", callback_data="get_vmess")],
    [InlineKeyboardButton("⚡ Obtenir VLESS", callback_data="get_vless")],
    [InlineKeyboardButton("🌐 Site Web", url=SITE_WEB), InlineKeyboardButton("💬 WhatsApp", url=WHATSAPP)]
]

# --- FONCTIONS DU BOT ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Salut bienvenue chez **IR MISSI ESPOIR** !\n\n"
        "Choisis ta configuration gratuite ci-dessous 👇\n"
        "Toujours connecté avec Airtel RDC 🇨🇩",
        reply_markup=InlineKeyboardMarkup(KEYBOARD),
        parse_mode="Markdown"
    )

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    if query.data == "get_vmess":
        await query.message.reply_text(
            f"✅ **Voici ta config VMESS :**\n\n`{VMESS_CONFIG}`\n\n"
            "👉 Copie et colle dans v2rayNG / NapsternetV\n"
            "Merci de choisir IR MISSI !",
            parse_mode="Markdown"
        )
    elif query.data == "get_vless":
        await query.message.reply_text(
            f"✅ **Voici ta config VLESS :**\n\n`{VLESS_CONFIG}`\n\n"
            "👉 Copie et colle dans v2rayNG / NapsternetV\n\n"
            "Merci de choisir IR MISSI !",
            parse_mode="Markdown"
        )

def main():
    if not BOT_TOKEN:
        print("ERREUR: BOT_TOKEN non trouvé dans Environment!")
        return
    
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_handler))
    
    print("Bot IR MISSI démarré...")
    application.run_polling()

if __name__ == "__main__":
    main()
