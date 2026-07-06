import pandas as pd
import ast
import pickle

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ----------------------------------------
# Helper Functions
# ----------------------------------------

def convert(text):
    L = []
    for i in ast.literal_eval(text):
        L.append(i['name'])
    return L


def convert3(text):
    L = []
    counter = 0

    for i in ast.literal_eval(text):
        if counter != 3:
            L.append(i['name'])
            counter += 1
        else:
            break

    return L


def fetch_director(text):
    L = []

    for i in ast.literal_eval(text):
        if i['job'] == 'Director':
            L.append(i['name'])
            break

    return L


# ----------------------------------------
# Load Dataset
# ----------------------------------------

movies = pd.read_csv("data/tmdb_5000_movies.csv")
credits = pd.read_csv("data/tmdb_5000_credits.csv")

# Merge datasets
movies = movies.merge(credits, on='title')

# Required columns
movies = movies[['movie_id',
                 'title',
                 'overview',
                 'genres',
                 'keywords',
                 'cast',
                 'crew']]

# Remove missing values
movies.dropna(inplace=True)

# Convert JSON columns
movies['genres'] = movies['genres'].apply(convert)
movies['keywords'] = movies['keywords'].apply(convert)
movies['cast'] = movies['cast'].apply(convert3)
movies['crew'] = movies['crew'].apply(fetch_director)

# Convert overview to list
movies['overview'] = movies['overview'].apply(lambda x: x.split())

# Remove spaces
movies['genres'] = movies['genres'].apply(lambda x: [i.replace(" ", "") for i in x])
movies['keywords'] = movies['keywords'].apply(lambda x: [i.replace(" ", "") for i in x])
movies['cast'] = movies['cast'].apply(lambda x: [i.replace(" ", "") for i in x])
movies['crew'] = movies['crew'].apply(lambda x: [i.replace(" ", "") for i in x])

# Create tags
movies['tags'] = movies['overview'] + movies['genres'] + movies['keywords'] + movies['cast'] + movies['crew']

# Keep required columns
new_df = movies[['movie_id', 'title', 'tags']]

# Convert list to string
new_df['tags'] = new_df['tags'].apply(lambda x: " ".join(x))

# Lowercase
new_df['tags'] = new_df['tags'].apply(lambda x: x.lower())

print("Creating TF-IDF Matrix...")

# TF-IDF
tfidf = TfidfVectorizer(stop_words='english', max_features=5000)

vectors = tfidf.fit_transform(new_df['tags'])

print("Calculating Similarity...")

similarity = cosine_similarity(vectors)

# Save Models
pickle.dump(new_df, open("model/movies.pkl", "wb"))
pickle.dump(similarity, open("model/similarity.pkl", "wb"))

print("\n====================================")
print("Movie Recommendation Model Created")
print("====================================")
print("Files Saved Successfully:")
print("model/movies.pkl")
print("model/similarity.pkl")
print("====================================")