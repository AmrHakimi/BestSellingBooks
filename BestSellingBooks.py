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
    Original_language = st.sidebar.selectbox('Original_language', ['Chinese', 'Czech', 'Dutch', 'English', 'French', 'German',
       'Gujarati', 'Hindi', 'Italian', 'Japanese', 'Norwegian',
       'Portuguese', 'Russian', 'Spanish', 'Swedish', 'Yiddish'])
    First_Published = st.sidebar.slider('First_Published', 0.3, 114, 20)
    Genre = st.sidebar.slider('Genre', 0.3, 114, 20)
    data = {'Authors': Authors,
            'Original_language': Original_language,
            'First_Published': First_Published
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
