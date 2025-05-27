import streamlit as st

st.title("🎈 selamat datang")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
st.image("2e57c48d2160c0c53738bfb63905bc75.jpg", width=200)
st.image("IMG-20250508-WA0042.jpg", width=200)

#st.title("Aplikasi Sederhana")
st.header("Aplikasi Mengecek Nilai Genap/Ganjil")
angka = st.number_input("Tulis sebuah Angka:", value=0, step=1)

if (angka % 2) == 0:
 st.write(f"{angka} adalah Bilangan Genap")
else:
 st.write(f"{angka} adalah Bilangan Ganjil")
