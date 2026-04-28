import streamlit as st 
import pickle 
import requests 

movies = pickle.load(open("movies.pkl", 'rb')) 
similarity = pickle.load(open("similarity.pkl", 'rb')) 

# finding movies
def find_movie(name):
    name = name.lower()
    for title in movies['title']:
        if name in title.lower():
            return title
    return None

# recommendations
def recommend(movie):
    movie = str(movie).lower().strip()
    movies['title'] = movies['title'].astype(str).str.lower().str.strip() 

    if movie not in movies['title'].values:
        return []

    index = movies[movies['title'] == movie].index[0]
    

    distances = similarity[index] 
    movie_list = sorted(
        list(enumerate(distances)), 
        reverse=True, 
        key=lambda x: x[1] 
    )[1:6] 

    results = []

    for i in movie_list:
        m = movies.iloc[i[0]] 
        results.append({
            "title": m.title,
            "genres": m.genres,
            "cast": m.cast,
            "director": m.director
        })

    return results


# API key
API_KEY = "add_your_api_key_here" 

def fetch_details(title):
    url = f"http://www.omdbapi.com/?t={title}&apikey={API_KEY}"
    data = requests.get(url).json()

    imdb_rating = data.get('imdbRating', 'N/A') 
    imdb_id = data.get('imdbID', '')
    imdb_url = f"https://www.imdb.com/title/{imdb_id}/"
    poster = data.get('Poster', '')

    return imdb_rating, imdb_url, poster


# UI
st.title("AI MOVIE RECOMMENDER")

movie_input = st.text_input("Enter a movie you liked:")

if st.button("Recommend"):
    movie = find_movie(movie_input)

    if movie is None:
        st.error("Movie not found")

    else:
        results = recommend(movie)

        if not results:
            st.error("No recommendations found")

        else:
            for r in results:
                imdb, url, poster = fetch_details(r['title'])

                st.markdown(f"## {r['title']}")
                st.image(poster)
                st.write(f"Genres: {', '.join(r['genres'])}")
                st.write(f"Director: {', '.join(r['director'])}")
                st.write(f"IMDb: {imdb}")

                st.markdown(f"[View on IMDb]({url})")
                st.markdown("---")
