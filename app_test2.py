import streamlit as st

st.image("logo9.png", caption="Logo Quiz", width=200)

question = "Apa ibu kota Indonesia?"
options = ["Jakarta", "Bandung", "Surabaya"]

answer = st.radio(question, options)

if st.button("Submit Jawaban"):
    if answer == "Jakarta":
        st.success("Jawaban kamu benar!")
    else:
        st.error("Jawaban salah, coba lagi!")