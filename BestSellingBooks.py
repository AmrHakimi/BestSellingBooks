import streamlit as st
import pandas as pd
import pickle


#mapping dictionary for datasets
genre_mapping
{
    31: 'Adventure', 47: 'Autobiographical novel', 25: 'Autobiography', 41: 'Bildungsroman, Historical fiction', 24: 'Biographical novel',
    26: "Children's Literature", 0: "Children's Literature, picture book", 19: "Children's fantasy novel", 42: "Children's fiction", 
    15: "Children's literature", 54: "Children's literature, picture book, fiction", 61: "Children's novel", 38: "Children's picture book", 
    45: 'Christian literature', 8: 'Classic regency novel, romance', 39: 'Coming-of-age', 11: 'Coming-of-age Murder mystery', 9: 'Crime novel', 
    35: 'Crime thriller novel', 72: 'Detective', 64: 'Dystopian fiction', 5: 'Dystopian, political fiction, social science fiction', 
    48: 'Erotica', 6: 'Essay/Literature', 23: 'Family saga', 67: 'Fantasy', 29: "Fantasy, Children's fiction", 
    52: 'Feminist novel', 49: 'Fiction', 43: 'Gothic horror, Family saga', 66: 'Gothic novel', 34: 'Historical fiction', 33: 'Historical fiction, war novel',
    56: 'Historical non-fiction, Autobiography, Memoir, Bildungsroman / Coming of Age, Jewish literature', 13: 'Historical novel',
    3: 'Historical novel, mystery', 46: 'Horror', 30: 'Japanese novel', 21: 'Magic realism', 28: 'Manual', 76: 'Memoir',
    77: 'Mystery', 62: 'Mystery thriller', 51: 'Mystery-thriller', 4: 'New-age spiritual novel', 44: 'Novel', 79: 'Novel, tragedy',
    68: 'Novella', 17: 'Novella, Self-help', 55: 'Philosophical novel, Young adult', 74: 'Picaresque novel, Bildungsroman, satire, Robinsonade',
    75: 'Popular science', 37: 'Popular science, Anthropology, Astrophysics, Cosmology, Philosophy, History', 60: 'Pregnancy guide', 2: 'Romance',
    18: 'Romance novel', 71: 'Romantic family saga', 58: 'Romantic novel', 63: 'Satirical allegorical novella, Political satire, Dystopian Fiction, Roman à clef',
    40: 'Science fiction', 10: 'Science fiction novel', 27: 'Self-help', 53: 'Self-help, motivational, business fable, psychology, leadership, parable',
    50: 'Semi-autobiographical novel', 78: 'Sexology', 14: 'Social Science, Anthropology, Psychology', 69: 'Socialist realist novel',
    70: 'Southern Gothic, Bildungsroman', 12: 'Thriller', 57: 'Travel literature', 7: 'Unfinished satirical dark comedy novel',
    65: 'War novel', 16: 'War, thriller', 1: 'Young Adult Fiction', 73: 'Young Adult novel, adventure, dystopian, science fiction',
    32: 'Young Adult novel, adventure, war, science fiction, action thriller', 22: 'Young adult fiction', 59: 'Young adult historical novel',
    20: 'Young adult novel', 36: 'Young adult romantic novel'

}


st.write("""
# Best Selling Books App

This app predicts the **Best Selling Books** type!
""")

st.sidebar.header('User Input Parameters')

def user_input_features():
    Authors = st.sidebar.selectbox('Authors Name',[ 22,   9,  58,   0,  17,  60,  16,  51, 146,  26, 115,  57, 126,
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
    Original_language = st.sidebar.selectbox('Original Language', [ 3,  4,  0,  7, 11, 13,  5,  8, 10, 12,  2, 14,  9,  1, 15,  6])
    First_Published = st.sidebar.selectbox('First Published', [ 4, 26, 75, 24,  2, 22, 32, 10, 70, 81, 76, 77, 78, 83, 85, 67, 33,
        7, 63, 47, 36, 28, 13,  6, 60, 55, 52, 56, 34, 12, 50, 49, 11, 40,
       59, 69, 17,  5,  8, 29, 57, 80, 46, 21, 15, 23, 31, 87, 86, 41, 27,
        1, 19, 68, 20, 71, 90, 92, 88, 38, 16, 54, 39, 82, 51, 65,  9, 62,
        3, 14, 43, 84, 53, 45, 44, 48, 94, 61, 73, 91, 89, 72, 25, 64, 79,
       18, 42, 37, 66, 30,  0, 58, 93, 35, 74])
    Genre = st.sidebar.selectbox('Genre', list.genre_mapping.key())
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
