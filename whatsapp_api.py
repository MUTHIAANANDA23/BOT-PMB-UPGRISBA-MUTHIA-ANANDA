from flask import Flask, request
import requests
from threading import Thread

# =====================================
# TOKEN FONNTE
# =====================================
TOKEN = "jFFc3VUSDEB7GHwiQqUf"

# =====================================
# FLASK
# =====================================
app_flask = Flask(__name__)

# =====================================
# WEBHOOK WHATSAPP
# =====================================
@app_flask.route("/webhook", methods=["POST"])
def webhook():

    # Ambil pesan masuk
    pesan = request.form.get("message", "").lower()

    # Ambil nomor pengirim
    nomor = request.form.get("sender")

    # =====================================
    # AUTO JAWAB
    # =====================================
    jawaban = "❌ Maaf pertanyaan belum tersedia."

    if "biaya" in pesan:

        jawaban = """
🎓 BIAYA KULIAH

Semester 1 : Rp 5.300.000
Semester 2-8 : Rp 2.950.000

SPP dapat dicicil 4x.
"""

    elif "beasiswa" in pesan:

        jawaban = """
🎓 BEASISWA

1. KIP-K
2. Prestasi
3. Roadshow
"""

    elif "jadwal" in pesan:

        jawaban = """
🎓 JADWAL PENDAFTARAN

Gelombang 1:
Januari - April 2026

Gelombang 2:
April - September 2026
"""

    elif "alamat" in pesan:

        jawaban = """
🎓 ALAMAT KAMPUS

UPGRISBA Padang
Jl. Gunung Pangilun
"""

    elif "prodi" in pesan:

        jawaban = """
🎓 PROGRAM STUDI

S1 SAINS DATA
"""

    elif "halo" in pesan:

        jawaban = """
👋 Halo calon mahasiswa UPGRISBA

Silakan tanyakan:
- biaya
- beasiswa
- jadwal
- alamat
- prodi
"""

    # =====================================
    # KIRIM BALASAN
    # =====================================
    requests.post(
        "https://api.fonnte.com/send",
        headers={
            "Authorization": TOKEN
        },
        data={
            "target": nomor,
            "message": jawaban
        }
    )

    return "OK"

# =====================================
# JALANKAN FLASK
# =====================================
def run_flask():
    app_flask.run(port=5000)

Thread(target=run_flask).start()