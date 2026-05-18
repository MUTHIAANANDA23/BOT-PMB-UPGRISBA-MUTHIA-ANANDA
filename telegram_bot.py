from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import Filters

TOKEN = "8674214268:AAGv697t2x1QL2MM6ZZwAE1mWHxdN0sA45M"

faq = {

    "biaya": "Biaya semester 1 Rp 5.300.000",

    "beasiswa": "Tersedia KIP-K",

    "jadwal": "Gelombang 1 Januari-April"
}

def start(update, context):

    update.message.reply_text(
        "Selamat datang di Chatbot PMB UPGRISBA"
    )

def balas(update, context):

    text = update.message.text.lower()

    jawaban = "Pertanyaan belum tersedia"

    for key in faq:

        if key in text:
            jawaban = faq[key]

    update.message.reply_text(jawaban)

updater = Updater(
    TOKEN,
    use_context=True
)

dp = updater.dispatcher

dp.add_handler(
    CommandHandler("start", start)
)

dp.add_handler(
    MessageHandler(
        Filters.text,
        balas
    )
)

updater.start_polling()

print("Bot Telegram Aktif...")

updater.idle()