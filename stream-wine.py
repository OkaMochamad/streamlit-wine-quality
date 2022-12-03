import pickle
import streamlit as st

# load save model
model = pickle.load(open('wine_model.sav', 'rb'))

# Judul Untuk Web
st.title('Prediksi Kualitas Wine')
st.text('Nama : Oka Mochamad Ocktafian Setiadi')
st.text('Nim : 191351184')
st.text('Matkul : Business Intelligence')
st.text('Keterangan : Untuk Inputan 0-3 Menandakan Kualitas Wine Buruk')
st.text('Inputan 4-6 Menandakan Kualitas Wine Sedang')
st.text('Inputan 7-10 Menandakan Kualitas Wine Baik')

#membagi kolom
col1, col2 = st.columns(2)

with col1:
    FixedAcidity = st.text_input ('Input nilai Fixed Acidity')

with col2:
    VolatileAcidity = st.number_input ('Input nilai Volatile Acidity')

with col1:
    CitricAcid = st.number_input ('Input nilai Citric Acid')

with col2:
    ResidualSugar = st.text_input('Input nilai ResidualSugar')

with col1:
    SugarChlorides = st.text_input('Input nilai Sugar Chlorides')

with col2:
    FreeSulfurDioxide = st.text_input('Input nilai Free Sulfur Dioxide')

with col1:
    TotalSulfurDioxide = st.text_input('Input nilai Total Sulfur Dioxide')

with col2:
    Density = st.text_input('Input nilai Density')

with col1:
    pH = st.text_input('Input nilai pH')

with col2:
    Sulphates = st.text_input('Input nilai Sulphates')

with col1:
    Alcohol = st.text_input('Input nilai Alcohol')

with col2:
    Id = st.text_input('Input nilai Id', 0, 1597, )

# code untuk prediksi
wine_quality = ''

# membuat tombol prediksi
if st.button('Test Prediksi Kualitas Wine') :
    wine_prediction = model.predict([[FixedAcidity, VolatileAcidity, CitricAcid, ResidualSugar, SugarChlorides, FreeSulfurDioxide, TotalSulfurDioxide, Density, pH, Sulphates, Alcohol, Id]])

    if(wine_prediction[0]==0):
        wine_quality = 'Kualitas Wine Buruk'
    elif(wine_prediction [0]==1):
        wine_quality = 'Kualitas Wine Buruk'
    elif(wine_prediction [0]==2):
        wine_quality = 'Kualitas Wine Buruk'
    elif(wine_prediction [0]==3):
        wine_quality = 'Kualitas Wine Buruk'
    elif(wine_prediction [0]==4):
        wine_quality = 'Kualitas Wine Sedang'
    elif(wine_prediction [0]==5):
        wine_quality = 'Kualitas Wine Sedang'
    elif(wine_prediction [0]==6):
        wine_quality = 'Kualitas Wine Baik'
    elif(wine_prediction [0]==7):
        wine_quality = 'Kualitas Wine Baik'
    elif(wine_prediction [0]==8):
        wine_quality = 'Kualitas Wine Baik'
    
st.success(wine_quality)
