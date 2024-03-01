import streamlit as st
import pandas as pd
import pickle

st.write("""
# Best Selling Books App

This app predicts the **Best Selling Books** type!
""")

st.sidebar.header('User Input Parameters')

def user_input_features():
    Authors = st.sidebar.selectbox('Author_Name',[ 22,   9,  58,   0,  17,  60,  16,  51, 146,  26, 115,  57, 126,
        87,  89,  47, 148,  72,  14,  90,   6, 144,  61, 121, 132,  33,
        59,  13, 122,  38,  35,  52, 145,  18,  78,  69, 108,  86,  19,
         7, 149,  24, 124,  85,  62,  15,  25,  44,  93,  28,  48, 150,
       136, 139, 125,   3, 133, 134,  63,  55,  84, 135, 103,  65,  74,
       114, 151, 131,  96,  41,  12,  56, 111,  49,  40,  21,  23,  71,
       153, 116, 128,  95,  10,  98, 137,  66, 142,  68, 100, 109, 120,
        39,  45,  30,  29, 141,  99, 107,  94, 101,   8,  34, 129, 130,
        64,  67,  83, 113,  75,  20,  70, 102,  31, 104,  43, 138,  91,
       106,  42, 119,  50,  88,  76,  53,   1, 110, 147,  27,  81,  73,
       152,  79,  11,  32,   5,  82,  77,   4,  80, 143,  36, 156,  92,
       140, 154, 123, 117,   2, 127,  97, 155, 112,  37, 118,  46, 105,
        54])
    st.write('Languages 3=Chinese, 4=Czech, 0=Dutch, 7=English, 11=French, 13=German, 5=Gujarati, 8=Hindi, 10=Italian, 12=Japanese, 2=Norwegian, 14=Portuguese, 9=Russian, 1=Spanish, 15=Swedish, 6=Yiddish')
    Original_language = st.sidebar.selectbox('Original_language', [ 3,  4,  0,  7, 11, 13,  5,  8, 10, 12,  2, 14,  9,  1, 15,  6])
    First_Published = st.sidebar.selectbox('First_Published', [ 4, 26, 75, 24,  2, 22, 32, 10, 70, 81, 76, 77, 78, 83, 85, 67, 33,
        7, 63, 47, 36, 28, 13,  6, 60, 55, 52, 56, 34, 12, 50, 49, 11, 40,
       59, 69, 17,  5,  8, 29, 57, 80, 46, 21, 15, 23, 31, 87, 86, 41, 27,
        1, 19, 68, 20, 71, 90, 92, 88, 38, 16, 54, 39, 82, 51, 65,  9, 62,
        3, 14, 43, 84, 53, 45, 44, 48, 94, 61, 73, 91, 89, 72, 25, 64, 79,
       18, 42, 37, 66, 30,  0, 58, 93, 35, 74])
    Genre = st.sidebar.selectbox('Genre', [31, 47, 25, 41, 24, 26,  0, 19, 42, 15, 54, 61, 38, 45,  8, 39, 11,
        9, 35, 72, 64,  5, 48,  6, 23, 67, 29, 52, 49, 43, 66, 34, 33, 56,
       13,  3, 46, 30, 21, 28, 76, 77, 62, 51,  4, 44, 79, 68, 17, 55, 74,
       75, 37, 60,  2, 18, 71, 58, 63, 40, 10, 27, 53, 50, 78, 14, 69, 70,
       12, 57,  7, 65, 16,  1, 73, 32, 22, 59, 20, 36])
    data = {'Authors': Authors,
            'Original_language': Original_language,
            'First_Published': First_Published,
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
