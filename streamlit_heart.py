import pickle 
import numpy as np
import streamlit as st

model = pickle.load(open('PrediksiHeart.sav', 'rb'))

st.title('Prediksi Penyakit')

col1, col2 = st.columns(2)

with col1 :
	Age = st.number_input('input Age')

	Sex= st.number_input('input Sex)')

	cp = st.number_input('input cp')

	trtbps = st.number_input('input trtbps')

with col2:
    chol = st.number_input('input chol')
    fbs= st.number_input('input fbs')
    restecg = st.number_input('input restecg')
    thalachh = st.number_input('input thalachh')
    exng = st.number_input('input exng')
    oldpeak = st.number_input('input oldpeak')
    slp = st.number_input('input slp')
    caa = st.number_input('input caa')
    thall = st.number_input('input thall')
prediksi = ''

if st.button('prediksi penyakit'):
	penyakit_prediksi = model.predict([[Age, Sex, cp, trtbps, chol, fbs, restecg, thalachh, exng, oldpeak, slp, caa, thall]])


# print(penyakit_prediksi)

	if(penyakit_prediksi[0]==1):
            prediksi = 'positif penyakit'
	else :
		prediksi = 'negatif  penyakit '
st.success(prediksi)