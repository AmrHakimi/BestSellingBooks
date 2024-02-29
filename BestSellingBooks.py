import streamlit as st
import pandas as pd
import pickle

st.write("""
# Best Selling Books App

This app predicts the **Best Selling Books** type!
""")

st.sidebar.header('User Input Parameters')

def user_input_features():
    Authors = st.sidebar.selectbox('Authors', )
    Original_language = st.sidebar.selectbox('Original_language,  3=Chinese,  4=Czech,  0=Dutch,  7=English, 11=French,
                                              13=German,  5=Gujarati,  8=Hindi, 10=Italian, 12=Japanese,  2=Norwegian, 14=Portuguese, 
                                              9=Russian,  1=Spanish, 15=Swedish,  6=Yiddish')
    First_Published = st.sidebar.slider('First_Published', 0.3, 114, 20)
    Genre = st.sidebar.slider('Genre', 0.3, 114, 20)
    data = {'Authors': Authors,
            'Original_language': Original language,
            'First_Published': First published
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
