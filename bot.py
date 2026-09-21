import os
import threading
from flask import Flask
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Petit serveur web pour Render
app = Flask(__name__)
@app.route('/')
def home():
    return "Bot Missi Espoir en ligne 24h/24"
def run_web():
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
threading.Thread(target=run_web, daemon=True).start()

# --- CONFIG IR MISSI ESPOIR (sécurisé) ---
BOT_TOKEN = os.environ.get("8856860220:AAGNpWFdb67qtMOaB1yTFs48E2AEUFVyBiU")
VMESS_LINK = os.environ.get("VMESS_LINK", "vmess://eyJhZGQiOiJ1cy0yMy5oaWh1Lm5ldCIsImFpZCI6IjAiLCJpZCI6IjM4ZTgxNjEwLWIwZDEtMTFmMS1iNzM5LTIwNWM2ZDVmNWQ3OCIsImhvc3QiOiJhaXJ0ZWxjYXJlYXBwLmFpcnRlbC5jZC51cy0yMy5oaWh1Lm5ldCIsIm5ldCI6IndzIiwicGF0aCI6Ii9lczh3ZzJuMyIsInBvcnQiOiI4MCIsInBzIjoiVm1lc3MgVVNBIFZpcmdpbmlhIDIwMjYtMDktMjIiLCJ0bHMiOiIiLCJ0eXBlIjoibm9uZSIsInYiOiIyIn0=")
VLESS_LINK = os.environ.get("VLESS_LINK", "vless://I_Love_🇵🇸_sshOcean_56e2@airtelcareapp.airtel.cd.us-23.hihu.net.fr1.v2less.online:443?encryption=none&security=tls&sni=fr1.v2less.online&type=grpc&serviceName=vless-grpc&mode=gun#sshocean-espoirmiss-gRPC")
SITE_WEB = "https://ir-missi-espoir.netlify.app"
WHATSAPP = "https://wa.me/243972104149"
NUMERO = "+243 972 104 149"
# -------------------------------

KEYBOARD = [
    ["🚀 Connexion Ultra VLESS", "⚡ Serveur VMess"],
    ["🌐 Serveur VLESS", "👤 Mon Abonnement Premium"],
    ["🎉 Essai Offert 24H", "💳 Activer Mon VIP"],
    ["📡 Statut des Serveurs", "🎓 Formation Pro VPN"],
    ["👨‍💼 Contact Admin"]
]
REPLY_MARKUP = ReplyKeyboardMarkup(KEYBOARD, resize_keyboard=True)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"👋 **Bienvenue sur le Bot Officiel IR MISSI ESPOIR** 🚀\n\n"
        f"Serveurs VMS / VLESS / VMess ultra rapides\n"
        f"Goma RDC - Ping bas pour Vodacom, Airtel, Orange\n\n"
        f"🌐 **Notre Site Officiel:**\n{SITE_WEB}\n\n"
        f"👇 **Clique sur un bouton :**",
        reply_markup=REPLY_MARKUP, parse_mode="Markdown"
    )

async def handle_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    t = update.message.text
    
    if t == "⚡ Serveur VMess":
        await update.message.reply_text(f"⚡ **Serveur VMess:**\n\n`{VMESS_LINK}`", parse_mode="Markdown")
    elif t == "🌐 Serveur VLESS":
        await update.message.reply_text(f"🌐 **Serveur VLESS:**\n\n`{VLESS_LINK}`", parse_mode="Markdown")
    elif t == "🚀 Connexion Ultra VLESS":
        await update.message.reply_text("🔒 **Accès VIP requis**\n\nTu dois payer l'abonnement pour avoir la connexion Ultra.\n\nClique sur 💳 Activer Mon VIP")
    elif t == "👤 Mon Abonnement Premium":
        await update.message.reply_text("📭 **Aucun abonnement trouvé**\n\nTu n'as aucun VIP actif.\nIl faut payer l'abonnement pour activer.")
    elif t == "💳 Activer Mon VIP":
        await update.message.reply_text(f"💳 **Activer VIP**\n\nContact Admin pour payer:\n{WHATSAPP}\nTel: {NUMERO}")
    elif t == "🎉 Essai Offert 24H":
        await update.message.reply_text("🎉 **Essai 24H**\n\nEssai bloqué - Paiement requis.\nContact Admin 👨‍💼")
    elif t == "📡 Statut des Serveurs":
        await update.message.reply_text(f"📡 **Statut:**\n🟢 VLESS: En ligne\n🟢 VMess: En ligne\n🌐 Site: {SITE_WEB}")
    elif t == "🎓 Formation Pro VPN":
        await update.message.reply_text(f"🎓 **Formation Pro VPN - 5000 FC**\n\nApprends à créer tes serveurs + site + bot comme moi\n\n📞 {NUMERO}\n💬 {WHATSAPP}")
    elif t == "👨‍💼 Contact Admin":
        await update.message.reply_text(
            f"👨‍💼 **IR MISSI ESPOIR - Contact**\n\n"
            f"🌐 Site: {SITE_WEB}\n"
            f"💬 WhatsApp: {WHATSAPP}\n"
            f"📞 Tel: {NUMERO}\n"
            f"✈️ Telegram: @IrMissi",
            parse_mode="Markdown"
        )

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_buttons))
    print("✅ Bot IR MISSI ESPOIR lancé !")
    app.run_polling()

if __name__ == "__main__":
    main()    elif t == "🌐 Serveur VLESS":
        await update.message.reply_text(f"🌐 **Serveur VLESS:**\n\n`{VLESS_LINK}`", parse_mode="Markdown")
    elif t == "🚀 Connexion Ultra VLESS":
        await update.message.reply_text("🔒 **Accès VIP requis**\n\nTu dois payer l'abonnement pour avoir la connexion Ultra.\n\nClique sur 💳 Activer Mon VIP")
    elif t == "👤 Mon Abonnement Premium":
        await update.message.reply_text("📭 **Aucun abonnement trouvé**\n\nTu n'as aucun VIP actif.\nIl faut payer l'abonnement pour activer.")
    elif t == "💳 Activer Mon VIP":
        await update.message.reply_text(f"💳 **Activer VIP**\n\nContact Admin pour payer:\n{WHATSAPP}\nTel: {NUMERO}")
    elif t == "🎉 Essai Offert 24H":
        await update.message.reply_text("🎉 **Essai 24H**\n\nEssai bloqué - Paiement requis.\nContact Admin 👨‍💼")
    elif t == "📡 Statut des Serveurs":
        await update.message.reply_text(f"📡 **Statut:**\n🟢 VLESS: En ligne\n🟢 VMess: En ligne\n🌐 Site: {SITE_WEB}")
    elif t == "🎓 Formation Pro VPN":
        await update.message.reply_text(f"🎓 **Formation Pro VPN - 5000 FC**\n\nApprends à créer tes serveurs + site + bot comme moi\n\n📞 {NUMERO}\n💬 {WHATSAPP}")
    elif t == "👨‍💼 Contact Admin":
        await update.message.reply_text(
            f"👨‍💼 **IR MISSI ESPOIR - Contact**\n\n"
            f"🌐 Site: {SITE_WEB}\n"
            f"💬 WhatsApp: {WHATSAPP}\n"
            f"📞 Tel: {NUMERO}\n"
            f"✈️ Telegram: @IrMissi",
            parse_mode="Markdown"
        )

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_buttons))
    print("✅ Bot IR MISSI ESPOIR lancé !")
    app.run_polling()

if __name__ == "__main__":
    main()
