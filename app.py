import streamlit as st
import pickle
import requests


movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))
movies_list= movies['title'].values
recommended_movies = []
recommended_movies_posters = []

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=c543d42210021e0463a5a4cfe0097a64&language=en-US'.format(movie_id))
    data = response.json()
    print(data)
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
    #find index of the movie, find the similarity index
    #sort the similarities, and get the top 5 from them
    #lets fetch the index
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse= True, key=lambda x: x[1])[1:6]
    #just sorting the similarities, without losing their index
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        #fetch poster from api

        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters


st.title('Movie Recommender System')
st.subheader('By Aditya Chauhan')
selected_movie = st.selectbox(
    '',
    movies_list)
if st.button("Recommend"):
    names,posters = recommend(selected_movie)
    import streamlit as st

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])

