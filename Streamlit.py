import streamlit as st

st.write("""
# Aplikasi Luas Bangun Datar
_Code dari latihan harian by Seazyn_
""")

choice = st.selectbox('Ingin Menghitung Bangun Datar Apa?', ('Luas Segitiga', 'Luas Persegi', 'Luas Layang-layang', 'Luas Lingkaran', 'Luas Trapesium'))

st.write('Program Hitung', choice)

if choice == 'Luas Segitiga':
    a = st.number_input('Masukkan Alas', 0)
    t = st.number_input('Masukkan Tinggi', 0)
    Button = st.button('Hitung')
    if Button:
        L = 0.5 * a * t
        st.success(f'\nHasil dari perhitungan Luas Bangun datar diatas adalah {L}')

elif choice == 'Luas Persegi':
    s = st.number_input('Masukkan Sisi : ', 0)
    Button = st.button('Hitung')
    if Button:
        L = s * s
        st.success(f'\nHasil dari perhitungan Luas Bangun datar diatas adalah {L}')

elif choice == 'Luas Layang-layang':
    d1 = st.number_input('Masukkan Diagonal 1 : ', 0)
    d2 = st.number_input('Masukkan Diagonal 2 : ', 0)
    Button = st.button('Hitung')
    if Button:
        L = 0.5 * d1 * d2
        st.success(f'\nHasil dari perhitungan Luas Bangun datar diatas adalah {L}')

elif choice == 'Luas Lingkaran':
    Phi = st.number_input('Masukkan Phi : ')
    r = st.number_input('Masukkan Jari-jari : ', 0)
    Button = st.button('Hitung')
    if Button:
        L = Phi * r**2
        st.success(f'\nHasil dari perhitungan Luas Bangun datar diatas adalah {L}')

elif choice == 'Luas Trapesium':
    a = st.number_input('Masukkan Sisi Sejajar a : ', 0)
    b = st.number_input('Masukkan Sisi Sejajar b : ', 0)
    t = st.number_input('Masukkan Tinggi         : ', 0)
    Button = st.button('Hitung')
    if Button:
        L = 0.5 * (a + b) * t
        print(f'\nHasil dari perhitungan Luas Bangun datar diatas adalah {L}')
