import streamlit as st

st.set_page_config(
    page_title="Multipage App",
    page_icon="👋",
)

st.title("Home")
st.sidebar.success("Pilih halaman di atas.")

st.subheader("Hai, Sahabat Ikan :wave:")
    
st.write(
        "Visi kami adalah menjadi sumber daya utama yang memberdayakan generasi milenial dalam mengembangkan pengetahuan, keterampilan, dan semangat kewirausahaan di bidang perikanan."
    )
st.write("[Website Kami](https://pranasiswa.gaeni.org/)")

st.write("---")

st.header("Apa yang Kami lakukan")
st.write("##")
st.write(
            """
            Di Aplikasi ini kita menerapkan DataScience sesuai dengan perkembangan zaman:
            - sedang mencari cara untuk belajar Python.
            - sedang mencari cara untuk belajar Streamlit.
            - ingin belajar Analisis Data & Ilmu Data untuk melakukan analisis.
            - ingin belajar Artificial Intelligence, Data Science, Machine Learning, Natural Language Processing.
            - ingin belajar dunia IT
            


            Jika Aplikasi ini menarik bagi Anda, jangan lupa untuk menghubungi kami.
            
            [Rumah Belajar Pranasiswa](https://pranasiswa.gaeni.org/index.html#contact)
            """
        )

footer = """
---

© 2023 Prediksi Kualitas Air
"""

st.markdown(footer)