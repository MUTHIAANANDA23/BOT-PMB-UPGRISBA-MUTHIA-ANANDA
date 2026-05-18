import streamlit as st
import pandas as pd
import os
from PIL import Image

# =========================
# KONFIGURASI HALAMAN
# =========================
st.set_page_config(
    page_title="Chatbot PMB UPGRISBA",
    page_icon="🎓",
    layout="wide"
)

# =========================
# CSS CUSTOM
# =========================
st.markdown("""
<style>

/* BACKGROUND */
.stApp {
    background:
    linear-gradient(
        rgba(255,255,255,0.78),
        rgba(255,255,255,0.78)
    ),
    url("https://images.unsplash.com/photo-1506744038136-46273834b3fb");

    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

/* HAPUS GARIS PUTIH */
.block-container {
    padding-top: 1rem;
}

header {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

/* PLANET */
.planet {
    position: fixed;
    top: 20px;
    right: 20px;
    width: 180px;
    z-index: 999;
    opacity: 0.95;
}

/* JUDUL */
.title-text {
    text-align: center;
    font-size: 50px;
    font-weight: bold;
    color: #0f172a;
    margin-top: 10px;
}

.sub-text {
    text-align: center;
    font-size: 24px;
    color: #1e3a8a;
    margin-bottom: 30px;
    font-weight: 600;
}

/* CARD */
.card {
    background: rgba(255,255,255,0.92);
    padding: 25px;
    border-radius: 25px;
    box-shadow: 0px 8px 25px rgba(0,0,0,0.2);
    margin-bottom: 25px;
    backdrop-filter: blur(5px);
}

/* SEMUA TEXT HITAM */
h1, h2, h3, h4, h5, h6,
p, label, div, span {
    color: black !important;
}

/* INPUT */
.stTextInput input {
    border-radius: 12px;
    border: 2px solid #2563eb;
    color: black;
    background-color: white;
}

/* SELECTBOX */
.stSelectbox div {
    color: black !important;
}

/* BUTTON */
.stButton>button {
    width: 100%;
    height: 50px;
    border-radius: 15px;
    border: none;
    font-size: 18px;
    font-weight: bold;
    background: linear-gradient(
        90deg,
        #2563eb,
        #60a5fa
    );
    color: white;
}

/* FORM BUTTON */
div.stForm button {
    width: 100%;
    background: linear-gradient(
        90deg,
        #1d4ed8,
        #3b82f6
    );
    color: white;
    border-radius: 15px;
    border: none;
    height: 50px;
    font-size: 18px;
    font-weight: bold;
}

/* DATAFRAME */
[data-testid="stDataFrame"] {
    background-color: white;
    border-radius: 15px;
    padding: 10px;
}

</style>
""", unsafe_allow_html=True)

# =========================
# GAMBAR PLANET
# =========================
st.markdown("""
<img class="planet"
src="https://pngimg.com/d/planet_PNG23.png">
""", unsafe_allow_html=True)

# =========================
# HEADER
# =========================
st.markdown("""
<div class="title-text">
🎓 CHATBOT PMB UPGRISBA
</div>

<div class="sub-text">
Program Studi S1 Sains Data
</div>
""", unsafe_allow_html=True)

# =========================
# TAMPILKAN BROSUR
# =========================
st.markdown('<div class="card">', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:

    try:
        brosur1 = Image.open(
            r"C:\Users\ASUS\Pictures\brosur1.png"
        )

        st.image(
            brosur1,
            caption="Brosur PMB 1",
            use_container_width=True
        )

    except Exception as e:
        st.error(f"Gagal membuka brosur1.png : {e}")

with col2:

    try:
        brosur2 = Image.open(
            r"C:\Users\ASUS\Pictures\brosur2.png"
        )

        st.image(
            brosur2,
            caption="Brosur PMB 2",
            use_container_width=True
        )

    except Exception as e:
        st.error(f"Gagal membuka brosur2.png : {e}")

st.markdown('</div>', unsafe_allow_html=True)

# =========================
# DATABASE FAQ
# =========================
faq = {

    "biaya": """
📌 BIAYA KULIAH

Semester 1 : Rp 5.300.000
Semester 2-8 : Rp 2.950.000

SPP dapat dicicil 4x.
""",

    "beasiswa": """
📌 BEASISWA

1. KIP-K
2. Jalur Prestasi
3. Jalur Roadshow
""",

    "jadwal": """
📌 JADWAL PENDAFTARAN

Gelombang 1:
Januari - April 2026

Gelombang 2:
April - September 2026
""",

    "pendaftaran": """
📌 PENDAFTARAN

Pendaftaran sudah dibuka.

Gelombang 1:
Januari - April 2026
""",

    "kapan": """
📌 PENDAFTARAN

Pendaftaran dimulai Januari 2026.
""",

    "mulai": """
📌 PENDAFTARAN

Pendaftaran dimulai Januari 2026.
""",

    "akreditasi": """
📌 AKREDITASI

Program Studi Sains Data
Terakreditasi Baik
""",

    "alamat": """
📌 ALAMAT KAMPUS

Universitas PGRI Sumatera Barat
Jl. Gunung Pangilun Padang
""",

    "prodi": """
📌 PROGRAM STUDI

S1 SAINS DATA
""",

    "kontak": """
📌 KONTAK

WhatsApp:
088742567464

Telegram:
@Pmbmuthiaanandaupgrisba_bot
"""
}

# =========================
# CHATBOT
# =========================
st.markdown('<div class="card">', unsafe_allow_html=True)

st.header("🤖 Chatbot PMB")

st.write("""
Contoh pertanyaan:
- biaya kuliah
- jadwal pendaftaran
- kapan mulai pendaftaran
- beasiswa
- alamat kampus
- prodi
""")

user_input = st.text_input(
    "Tanyakan sesuatu..."
)

if user_input:

    pertanyaan = user_input.lower()

    jawaban = "❌ Maaf, pertanyaan belum tersedia."

    ditemukan = False

    for key in faq:

        if key in pertanyaan:
            jawaban = faq[key]
            ditemukan = True
            break

    if not ditemukan:

        if "daftar" in pertanyaan:
            jawaban = faq["pendaftaran"]

        elif "kuliah" in pertanyaan:
            jawaban = faq["biaya"]

        elif "kampus" in pertanyaan:
            jawaban = faq["alamat"]

    st.success(jawaban)

st.markdown('</div>', unsafe_allow_html=True)

# =========================
# KONTAK
# =========================
st.markdown('<div class="card">', unsafe_allow_html=True)

st.header("📲 Hubungi Kami")

col1, col2 = st.columns(2)

with col1:

    st.markdown("""
    <a href="https://wa.me/6288742567464" target="_blank">
        <button style="
            background:#25D366;
            color:white;
            padding:15px;
            width:100%;
            border:none;
            border-radius:12px;
            font-size:18px;
            font-weight:bold;
            cursor:pointer;">
            WhatsApp Admin
        </button>
    </a>
    """, unsafe_allow_html=True)

with col2:

    st.markdown("""
    <a href="https://t.me/Pmbmuthiaanandaupgrisba_bot" target="_blank">
        <button style="
            background:#0088cc;
            color:white;
            padding:15px;
            width:100%;
            border:none;
            border-radius:12px;
            font-size:18px;
            font-weight:bold;
            cursor:pointer;">
            Telegram Bot
        </button>
    </a>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# =========================
# FORM PENDAFTARAN
# =========================
st.markdown('<div class="card">', unsafe_allow_html=True)

st.header("📝 Form Pendaftaran")

with st.form("form_pendaftaran"):

    nama = st.text_input("Nama Lengkap")

    hp = st.text_input("Nomor HP")

    asal = st.text_input("Asal Sekolah")

    jurusan = st.selectbox(
        "Pilih Jurusan",
        ["Sains Data"]
    )

    submit = st.form_submit_button("DAFTAR")

    if submit:

        os.makedirs(
            "database",
            exist_ok=True
        )

        data = {
            "Nama": [nama],
            "HP": [hp],
            "Asal Sekolah": [asal],
            "Jurusan": [jurusan]
        }

        df = pd.DataFrame(data)

        file = "database/data.csv"

        if os.path.exists(file):

            df.to_csv(
                file,
                mode='a',
                header=False,
                index=False
            )

        else:

            df.to_csv(
                file,
                index=False
            )

        st.success("✅ Pendaftaran Berhasil!")

st.markdown('</div>', unsafe_allow_html=True)

# =========================
# DATA PENDAFTAR
# =========================
st.markdown('<div class="card">', unsafe_allow_html=True)

st.header("📊 Data Pendaftar")

if os.path.exists("database/data.csv"):

    data = pd.read_csv(
        "database/data.csv"
    )

    st.dataframe(
        data,
        use_container_width=True
    )

else:
    st.warning("Belum ada data.")

st.markdown('</div>', unsafe_allow_html=True)