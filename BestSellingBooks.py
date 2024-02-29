import streamlit as st
import pandas as pd
import pickle

st.write("""
# Best Selling Books App

This app predicts the **Best Selling Books** type!
""")

st.sidebar.header('User Input Parameters')

def user_input_features():
    Author(s) = st.sidebar.slider('Author(s)', 0.7, 297, 100)
    Original language = st.sidebar.slider('Original language', 0, 50, 15)
    First published = st.sidebar.slider('First published', 0.3, 114, 20)
    Genre = st.sidebar.slider('Genre', 0.3, 114, 20)
    data = {'Author(s)': Author(s),
            'Original language': Original language,
            'First published': First published
            'Genre': Genre}
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader('User Input parameters')
st.write(df)

loaded_model = pickle.load(open("Best_Selling_Bookss.h5", "rb"))

prediction = loaded_model.predict(df)

st.subheader('Prediction')
st.write(prediction)
