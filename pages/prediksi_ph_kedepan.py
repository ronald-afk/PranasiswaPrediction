import pickle
import streamlit as st 
import pandas as pd 
import matplotlib.pyplot as plt 

model = pickle.load(open('pages/prediksi_ph_kedepan.sav', 'rb'))
st.sidebar.success("Pilih halaman di atas.")


df = pd.read_csv('pages/airnov.csv', delimiter=';', usecols=['Tanggal', 'pH'])
df['Tanggal'] = pd.to_datetime(df['Tanggal'])
df.set_index(['Tanggal'], inplace=True)

st.title('Perkiraan Kualitas pH')
year = st.slider('Tentukan Hari', 1, 30, step=1)
pred = model.forecast(year)  # Ganti Tanggal dengan year
pred = pd.DataFrame(pred, columns=['pH'])

if st.button('Predict'):
    col1, col2 = st.columns([2, 3])
    with col1:
        st.dataframe(pred)

    with col2:
        fig, ax = plt.subplots()
        df['pH'].plot(style='', color='gray', legend=True, label='known')
        pred['pH'].plot(color='b', legend=True, label='Prediction')
        st.pyplot(fig)

footer = """
---

© 2023 Prediksi Kualitas Air
"""

st.markdown(footer)