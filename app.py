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
    for i in list_of_movie,list_of_rating,list_of_description:
        st.write(st.header(list_of_movie[i]),
        st.subheader(list_of_rating[i]),
        st.caption(list_of_description[i]))