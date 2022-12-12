import streamlit as st

st.write("""
# Aplikasi Luas Segitiga
Ini adalah Aplikasi Menghitung Luas Segitiga Sederhana Menggunakan Streamlit
""")

alas   = st.number_input("Masukkan Alas",0)
tinggi = st.number_input("Masukkan Tinggi",0)
hitung = st.button('Hitung Luas')

if hitung:
    luas = 0.5 * alas * tinggi
    st.success(f"Luas dari segitiga tersebut adalah {luas}")




















