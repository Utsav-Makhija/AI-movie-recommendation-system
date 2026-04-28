import pandas as pd
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#loading info from dataset
movies = pd.read_csv('TMDB_all_movies')

#selecting and accessing relevent columns from the dataset
movies = movies[['id' , 'title' , 'overview' , 'genres' , 'cast' , 'director' , 'imdb_rating']]

#removing missing values
movies.dropna(inplace=True)

movies = movies.head(10000) #limits to top 10000 movies


def split_text(text):
    return text.split('|')

#applying split to all relevent data columns:
movies['genres'] = movies['genres'].apply(split_text)
movies['cast'] = movies['cast'].apply(split_text)
movies['director'] = movies['director'].apply(split_text)


movies['cast'] = movies['cast'].apply(lambda x: x[:3])


def create_tages(row):
    return(
        " ".join(row['genres']) * 3 + ' ' +
        " ".join(row['cast']) * 2 + " " +
        " ".join(row['director']) * 2 + " " +
        row['overview']
    )

#applying tags:

movies['tags'] = movies.apply(create_tages , axis = 1) 

movies['tags'] = movies['tags'].apply(lambda x: x.lower()) 

#vectorization:

cv = CountVectorizer(max_features = 5000 , stop_words = 'english')
vectors = cv.fit_transform(movies['tags']).toarray()


similarity = cosine_similarity(vectors)


#creating save files
pickle.dump(movies , open('movies.pkl' , 'wb'))
pickle.dump(similarity , open('similarity.pkl' , 'wb'))


print('MODEL BUILT SUCCESSFULLY')
