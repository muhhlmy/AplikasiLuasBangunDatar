import streamlit as st

st.write("""
# Aplikasi Program Warnet
Ini adalah tugas kedua dari Matkul yang telah saya selesaikan
""")

Jam = st.input_number("Ingin Menyewa berapa jam? : ")

if Jam <= 3:
    Biaya = (Jam * 6000)
    st.write("Biaya yang harus dibayar adalah : " + str(Biaya))

elif Jam > 3:
    Biaya = (18000 + ((Jam - 3) * 5000))
    st.write("Biaya yang harus dibayar adalah : " + str(Biaya))
