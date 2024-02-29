import streamlit as st
import pandas as pd
import pickle
from sklearn import preprocessing.LabelEncoder()
st.write("""
# Best Selling Books App

This app predicts the **Best Selling Books** type!
""")

st.sidebar.header('User Input Parameters')

def user_input_features():
    Authors = st.sidebar.selectbox('Authors',['Agatha Christie', 'Albert Camus', 'Alex Comfort',
       'Alexander Alexandrovich Fadeyev', 'Alice Sebold', 'Andrew Morton',
       'Anna Sewell', 'Anne Frank', 'Anthony Doerr',
       'Antoine de Saint-Exupéry', 'Arlene Eisenberg and Heidi Murkoff',
       'Astrid Lindgren', 'Banana Yoshimoto', 'Beatrix Potter',
       'Benjamin Spock', 'Bill Wilson', 'C. S. Lewis', 'Cao Xueqin',
       'Carl Sagan', 'Carlo Collodi', 'Carlos Ruiz Zafón',
       'Charles Berlitz', 'Charles Dickens', 'Chinua Achebe',
       'Colleen McCullough', 'Dale Carnegie', 'Dan Brown',
       'Dante Alighieri', 'Daphne du Maurier', 'Delia Owens',
       'Desmond Morris', 'Douglas Adams', 'Dr. Seuss',
       'E. B. White; illustrated by Garth Williams', 'E. L. James',
       'Elbert Hubbard', 'Elie Wiesel', 'Eliyahu M. Goldratt',
       'Eric Carle', 'Erica Jong', 'Erich Maria Remarque', 'Erich Segal',
       'Ernest Hemingway', 'Erskine Caldwell', 'F. Scott Fitzgerald',
       'Frank Herbert', 'Frank McCourt', 'Gabriel García Márquez',
       'George Orwell', 'Gillian Flynn', 'Grace Metalious',
       'H. Rider Haggard', 'Harper Lee', 'Haruki Murakami',
       'Helen Fielding', 'Irving Stone', 'Ivan Yefremov',
       'J. D. Salinger', 'J. K. Rowling', 'J. P. Donleavy',
       'J. R. R. Tolkien', 'Jack Higgins', 'Jacqueline Susann',
       'Jacques-Henri Bernardin de Saint-Pierre', 'James Clavell',
       'James Redfield', 'Jane Austen', 'Janette Sebring Lowrey',
       'Jaroslav Hašek', 'Jeffrey Archer', 'Jhumpa Lahiri', 'Jiang Rong',
       'Johanna Spyri', 'John Boyne', 'John Green', 'John Steinbeck',
       'Jojo Moyes', 'Joseph Heller', 'Jostein Gaarder',
       'Julia Donaldson', 'Jung Chang', 'Kahlil Gibran',
       'Kathryn Stockett', 'Ken Follett', 'Kenneth Grahame',
       'Khaled Hosseini', 'Leo Tolstoy', 'Lew Wallace', 'Lois Lowry',
       'Louise Hay', 'Lucy Maud Montgomery', "Madeleine L'Engle",
       'Marabel Morgan', 'Margaret Mitchell', 'Margaret Wise Brown',
       'Marilyn French', 'Mario Puzo', 'Mark Manson', 'Mark Twain',
       'Markus Zusak', 'Maurice Sendak', 'Michael Ende', 'Michelle Obama',
       'Mikhail Sholokhov', 'Mitch Albom', 'Mohandas Karamchand Gandhi',
       'Nelson Mandela', 'Nicholas Evans', 'Nikolai Ostrovsky',
       'Norman Vincent Peale', 'Osamu Dazai', 'Paramahansa Yogananda',
       'Patricia Nell Warren', 'Patrick Süskind', 'Paula Hawkins',
       'Paulo Coelho', 'Peter Benchley', 'Pierre Dukan', 'Ray Bradbury',
       'Raymond Moody', 'Rhonda Byrne', 'Richard Adams', 'Richard Bach',
       'Richard Nelson Bolles', 'Rick Warren', 'Roald Dahl',
       'Robert James Waller', 'Robert L. Short', 'Robert Munsch',
       'S. E. Hinton', 'Sam McBratney', 'Sergey Mikhalkov', 'Shere Hite',
       'Spencer Johnson', 'Stephen Hawking', 'Stephen R. Covey',
       'Stieg Larsson', 'Sue Townsend', 'Susanna Tamaro',
       'Suzanne Collins', 'Taichi Sakaiya', 'Tetsuko Kuroyanagi',
       'Thor Heyerdahl', 'Tomás Eloy Martínez', 'Umberto Eco',
       'V. C. Andrews', 'Ved Prakash Sharma', 'Viktor Frankl',
       'Vladimir Nabokov', 'Wayne Dyer', 'William Bradford Huie',
       'William P. Young', 'William Peter Blatty', 'Xaviera Hollander',
       'Xue Muqiao', 'Yann Martel', 'Yu Dan')
    authors_encoded=label_encoder.fit_transform(Authors) 
    Original_language = st.sidebar.selectbox('Original_language', ['Chinese', 'Czech', 'Dutch', 'English', 'French', 'German',
       'Gujarati', 'Hindi', 'Italian', 'Japanese', 'Norwegian',
       'Portuguese', 'Russian', 'Spanish', 'Swedish', 'Yiddish'])
    language_encoded=label_encoder.fit_transform(Original_language) 
    First_Published = st.sidebar.selectbox('First_Published', [1304, 1788, 1791, 1813, 1859, 1869, 1877, 1880, 1881, 1885, 1887,
       1899, 1902, 1908, 1923, 1925, 1929, 1932, 1933, 1934, 1935, 1936,
       1937, 1938, 1939, 1942, 1943, 1945, 1946, 1947, 1948, 1949, 1950,
       1951, 1952, 1953, 1955, 1956, 1957, 1958, 1960, 1961, 1962, 1963,
       1964, 1965, 1966, 1967, 1968, 1969, 1970, 1971, 1972, 1973, 1974,
       1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1984, 1985, 1986,
       1987, 1988, 1989, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998,
       1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009,
       2010, 2011, 2012, 2014, 2015, 2016, 2018])
    firstpublished_encoded=label_encoder.fit_transform(First_Published) 
    Genre = st.sidebar.selectbox('Genre', ['Adventure', 'Autobiographical novel', 'Autobiography',
       'Bildungsroman, Historical fiction', 'Biographical novel',
       "Children's Literature", "Children's Literature, picture book",
       "Children's fantasy novel", "Children's fiction",
       "Children's literature",
       "Children's literature, picture book, fiction", "Children's novel",
       "Children's picture book", 'Christian literature',
       'Classic regency novel, romance', 'Coming-of-age',
       'Coming-of-age Murder mystery', 'Crime novel',
       'Crime thriller novel', 'Detective', 'Dystopian fiction',
       'Dystopian, political fiction, social science fiction', 'Erotica',
       'Essay/Literature', 'Family saga', 'Fantasy',
       "Fantasy, Children's fiction", 'Feminist novel', 'Fiction',
       'Gothic horror, Family saga', 'Gothic novel', 'Historical fiction',
       'Historical fiction, war novel',
       'Historical non-fiction, Autobiography, Memoir, Bildungsroman / Coming of Age, Jewish literature',
       'Historical novel', 'Historical novel, mystery', 'Horror',
       'Japanese novel', 'Magic realism', 'Manual', 'Memoir', 'Mystery',
       'Mystery thriller', 'Mystery-thriller', 'New-age spiritual novel',
       'Novel', 'Novel, tragedy', 'Novella', 'Novella, Self-help',
       'Philosophical novel, Young adult',
       'Picaresque novel, Bildungsroman, satire, Robinsonade',
       'Popular science',
       'Popular science, Anthropology, Astrophysics, Cosmology, Philosophy, History',
       'Pregnancy guide', 'Romance', 'Romance novel',
       'Romantic family saga', 'Romantic novel',
       'Satirical allegorical novella, Political satire, Dystopian Fiction, Roman à clef',
       'Science fiction', 'Science fiction novel', 'Self-help',
       'Self-help, motivational, business fable, psychology, leadership, parable',
       'Semi-autobiographical novel', 'Sexology',
       'Social Science, Anthropology, Psychology',
       'Socialist realist novel', 'Southern Gothic, Bildungsroman',
       'Thriller', 'Travel literature',
       'Unfinished satirical dark comedy novel', 'War novel',
       'War, thriller', 'Young Adult Fiction',
       'Young Adult novel, adventure, dystopian, science fiction',
       'Young Adult novel, adventure, war, science fiction, action thriller',
       'Young adult fiction', 'Young adult historical novel',
       'Young adult novel', 'Young adult romantic novel'])
    genre_encoded=label_encoder.fit_transform(Genre) 
    data = {'Authors': authors_encoded,
            'Original_language': language_encoded,
            'First_Published': firstpublished_encoded,
            'Genre': genre_encoded}
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader('User Input parameters')
st.write(df)

loaded_model = pickle.load(open("Best_Selling_Bookss.h5", "rb"))

prediction = loaded_model.predict(df)

st.subheader('Prediction')
st.write(prediction)
