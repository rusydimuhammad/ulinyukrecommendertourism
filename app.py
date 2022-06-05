import streamlit as st
import pickle
import pandas as pd

def recommend(place):
  model_df = similarity
  model_df = pd.DataFrame(model_df, index=data_tourism_new['Place_Name'], columns=data_tourism_new['Place_Name'])
  count = 6
  items=data_tourism_new[['Place_Name','Description','Rating']]
  index = model_df.loc[:,place].to_numpy().argpartition(range(-1, -count, -1))
  closest = model_df.columns[index[-1:-(count+2):-1]]
  closest = closest.drop(place, errors='ignore')
  new_rec = pd.DataFrame(closest).merge(items).head(count)

  list_of_movie = new_rec['Place_Name'].tolist()
  list_of_rating = new_rec['Rating'].tolist()
  list_of_description = new_rec['Description'].tolist()

  return list_of_movie,list_of_rating,list_of_description

place_dict = pickle.load(open('place_dict.pkl','rb'))
places = pd.DataFrame(place_dict)
similarity = pickle.load(open('similarity.pkl','rb'))
data_tourism_new = pickle.load(open('data_tourism_new.pkl','rb'))
data_tourism_new = pd.DataFrame(data_tourism_new)

st.title('Sistem Rekomendasi Destinasi Wisata di Bandung')
option = st.selectbox(
    "Pilih tempat yang Anda suka!",
    places['Place_Name'].values
)

if st.button('Rekomendasi'):
    list_of_movie,list_of_rating,list_of_description = recommend(option)
    col1 = st.columns(1)
    with col1:
        st.header(list_of_movie[0])
        st.subheader(list_of_rating[0])
        st.caption(list_of_description[0])
    with col1:
        st.header(list_of_movie[1])
        st.subheader(list_of_rating[1])
        st.caption(list_of_description[1])
    with col1:
        st.header(list_of_movie[2])
        st.subheader(list_of_rating[2])
        st.caption(list_of_description[2])
    with col1:
        st.header(list_of_movie[3])
        st.subheader(list_of_rating[3])
        st.caption(list_of_description[3])
    with col1:
        st.header(list_of_movie[4])
        st.subheader(list_of_rating[4])
        st.caption(list_of_description[4])
    with col1:
        st.header(list_of_movie[5])
        st.subheader(list_of_rating[5])
        st.caption(list_of_description[5])