# AI Movie Recommendation System

An AI-powered movie recommendation system built using Python, Machine Learning, and Streamlit.
This project suggests movies based on user input by analyzing content similarity such as genres, cast, director, and overview.

## Features
- Search for a movie you like
- Get top 5 similar movie recommendations
- Content-based filtering using ML
- Fetch IMDb ratings dynamically
- Display movie posters
- Direct link to IMDb pages

## How It Works
This project uses a content-based recommendation system

- Movie data is processed and cleaned
- Important features like:
  1.  Genres
  2.  Cast (top 3 actors)
  3.  Director
  4.  Overview

  are combined into a single text representation ("tags")
- Text is converted into numerical vectors using CountVectorizer
- Similarity between movies is calculated using cosine similarity
- The most similar movies are recommended to the user

## Tech Stack:
- Python
- Pandas
- Scikit-learn
- Streamlit
- Pickle
- Requests (OMDb API)

## Project Structure
-  app.py              # Streamlit web app (UI + recommendations)
-  model.py            # Data processing & model building
-  movies.pkl          # Processed movie dataset
-  similarity.pkl      # Similarity matrix
-  TMDB_all_movies     # Dataset file


## API Used
OMDb API (for IMDb ratings, posters, and links)

You can get your own API key from:
👉 http://www.omdbapi.com/

## Replace in app.py:

API_KEY = "your_api_key_here"

## Limitations
- Works only on available dataset (top ~10,000 movies)
- Recommendations are based on content, not user preferences
- Requires exact or partial movie name match
## Future Improvements
- Add collaborative filtering
- Improve search with fuzzy matching
- Deploy on cloud (Streamlit Cloud / AWS / Render)
- Add user login & watch history
- Enhance UI/UX
## Author
Utsav Makhija
## License

This project is for **educational purposes**.
