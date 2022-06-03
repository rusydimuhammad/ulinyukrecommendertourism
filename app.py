import streamlit as st
import pickle
import pandas as pd

def recommend(place):
    index = data_tourism[data_tourism['Place_Name'] == place].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_place = []
    for i in distances[1:6]:
        recommended_place.append(data_tourism.iloc[i[0]].Place_Name)
    return recommended_place

place_dict = pickle.load(open('place_dict.pkl','rb'))
places = pd.DataFrame(place_dict)
similarity = pickle.load(open('similarity.pkl','rb'))
data_tourism = pickle.load(open('data_tourism.pkl','rb'))
data_tourism = pd.DataFrame(data_tourism)

st.title('Sistem Rekomendasi Destinasi Wisata')
option = st.selectbox(
    "Pilih tempat yang Anda suka!",
    places['Place_Name'].values
)

if st.button('Rekomendasi'):
    recommendations = recommend(option)
    for i in recommendations:
        st.write(i)