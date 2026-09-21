import os
import threading
from flask import Flask
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

app = Flask(__name__)
@app.route('/')
def home():
    return "Bot IR MISSI ESPOIR 24h/24 en ligne"
def run_web():
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
threading.Thread(target=run_web, daemon=True).start()

# --- TOKEN ANCIEN MIS ICI COMME TU AS DEMANDÉ ---
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8856860220:AAGNpWFdb67qtMOaB1yTFs48E2AEUFVyBiU")

VLESS_80 = "vless://I_Love_🇵🇸_sshOcean_987f@airtelcareapp.airtel.cd.us-23.hihu.net.nl1.v2less.online:80?encryption=none&security=none&type=ws&host=nl1.v2less.online&path=%2Fvless#sshocean-missie-ws"
VLESS_443 = "vless://I_Love_🇵🇸_sshOcean_987f@airtelcareapp.airtel.cd.us-23.hihu.net.nl1.v2less.online:443?encryption=none&security=tls&sni=airtelcareapp.airtel.cd.us-23.hihu.net&type=httpupgrade&host=nl1.v2less.online&path=%2Fhttpupgrade#sshocean-missie-httpupgrade"
VMESS_80 = "vmess://eyJhZGQiOiJhaXJ0ZWxjYXJlYXBwLmFpcnRlbC5jZC51cy0yMy5oaWh1Lm5ldCIsImFpZCI6IjAiLCJpZCI6ImM4MjkxNTYwLWI1ZjktMTFmMS1iNzM1LTIwNWM2ZDVmNWQ3OCIsImhvc3QiOiJ1cy0yMy5oaWh1Lm5ldCIsIm5ldCI6IndzIiwicGF0aCI6Ii9zM3dyajVwdiIsInBvcnQiOiI4MCIsInBzIjoiUjgwOlZtZXNzIFVTQSBWaXJnaW5pYSAyMDI2LTA5LTI5IiwidGxzIjoiIiwidHlwZSI6Im5vbmUiLCJ2IjoiMiJ9"
VMESS_443 = "vmess://eyJhZGQiOiJhaXJ0ZWxjYXJlYXBwLmFpcnRlbC5jZC51cy0yMy5oaWh1Lm5ldCIsImFpZCI6IjAiLCJpZCI6ImM4MjkxNTYwLWI1ZjktMTFmMS1iNzM1LTIwNWM2ZDVmNWQ3OCIsImhvc3QiOiJ1cy0yMy5oaWh1Lm5ldCIsIm5ldCI6IndzIiwicGF0aCI6Ii9zM3dyajVwdiIsInBvcnQiOiI0NDMiLCJwcyI6IlI0NDM6Vm1lc3MgVVNBIFZpcmdpbmlhIDIwMjYtMDktMjkiLCJ0bHMiOiJ0bHMiLCJ0eXBlIjoibm9uZSIsInYiOiIyIn0="

SITE_WEB = "https://ir-missi-espoir.netlify.app"
WHATSAPP = "https://wa.me/243972104149"
NUMERO = "+243 972 104 149"

MAIN_KEYBOARD = [["🌐 Serveur VLESS", "⚡ Serveur VMess"], ["🔐 Serveur SSH", "📡 Statut des Serveurs"], ["🎓 Formation Pro VPN", "👨‍💼 Contact Admin"]]
VLESS_KEYBOARD = [["🌐 VLESS Port 80", "🌐 VLESS Port 443"], ["⬅️ Retour Menu"]]
VMESS_KEYBOARD = [["⚡ VMess Port 80", "⚡ VMess Port 443"], ["⬅️ Retour Menu"]]

MAIN_MARKUP = ReplyKeyboardMarkup(MAIN_KEYBOARD, resize_keyboard=True)
VLESS_MARKUP = ReplyKeyboardMarkup(VLESS_KEYBOARD, resize_keyboard=True)
VMESS_MARKUP = ReplyKeyboardMarkup(VMESS_KEYBOARD, resize_keyboard=True)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"👋 **IR MISSI ESPOIR** 🚀\n🌐 {SITE_WEB}\n\n👇 Choisis ton serveur :", reply_markup=MAIN_MARKUP, parse_mode="Markdown")

async def handle_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    t = update.message.text
    if t == "🌐 Serveur VLESS":
        await update.message.reply_text("🌐 **Choisis PORT VLESS:**", reply_markup=VLESS_MARKUP, parse_mode="Markdown")
    elif t == "⚡ Serveur VMess":
        await update.message.reply_text("⚡ **Choisis PORT VMess:**", reply_markup=VMESS_MARKUP, parse_mode="Markdown")
    elif t == "🌐 VLESS Port 80":
        await update.message.reply_text(f"🌐 **VLESS 80**\n\n`{VLESS_80}`", parse_mode="Markdown")
    elif t == "🌐 VLESS Port 443":
        await update.message.reply_text(f"🌐 **VLESS 443**\n\n`{VLESS_443}`", parse_mode="Markdown")
    elif t == "⚡ VMess Port 80":
        await update.message.reply_text(f"⚡ **VMess 80**\n\n`{VMESS_80}`", parse_mode="Markdown")
    elif t == "⚡ VMess Port 443":
        await update.message.reply_text(f"⚡ **VMess 443**\n\n`{VMESS_443}`", parse_mode="Markdown")
    elif t == "🔐 Serveur SSH":
        await update.message.reply_text(f"🔐 **SSH IR MISSI**\n\nHostname: `de1.sshweb.site`\nNameserver: `de1.ns.sshweb.site`\nUsername: `sshocean-missi028`\nPassword: `28394`\nPort: `22`\n\nPayload:\n`HTTP/1.1 200[crlf]Host: irmissiespoir.com[crlf]X-Online-Host: irmissiespoir.com[crlf]`\n\nExpire: 29 Sep 2026", parse_mode="Markdown")
    elif t == "⬅️ Retour Menu":
        await update.message.reply_text("⬅️ Menu principal", reply_markup=MAIN_MARKUP)
    elif t == "📡 Statut des Serveurs":
        await update.message.reply_text(f"📡 **Statut:**\n🟢 VLESS 80: OK\n🟢 VLESS 443: OK\n🟢 VMess 80: OK\n🟢 VMess 443: OK\n🟢 SSH: OK\n🌐 {SITE_WEB}")
    elif t == "🎓 Formation Pro VPN":
        await update.message.reply_text(f"🎓 **Formation 5000 FC**\n{WHATSAPP}")
    elif t == "👨‍💼 Contact Admin":
        await update.message.reply_text(f"👨‍💼 **IR MISSI**\n🌐 {SITE_WEB}\n💬 {WHATSAPP}\n📞 {NUMERO}")

def main():
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_buttons))
    print("✅ Bot IR MISSI 5 serveurs lancé !")
    application.run_polling()

if __name__ == "__main__":
    main()
