import pickle

# Load trained model
movies = pickle.load(open("model/movies.pkl", "rb"))
similarity = pickle.load(open("model/similarity.pkl", "rb"))


def recommend(movie_name):
    """
    Returns top 5 recommended movies.
    """

    movie_name = movie_name.strip()

    # Check whether movie exists
    if movie_name not in movies['title'].values:
        return None

    # Get movie index
    movie_index = movies[movies['title'] == movie_name].index[0]

    # Similarity scores
    distances = similarity[movie_index]

    # Sort by similarity
    movie_list = sorted(
        enumerate(distances),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommendations = []

    for movie in movie_list:
        recommendations.append(
            movies.iloc[movie[0]].title
        )

    return recommendations


def get_movie_titles():
    """
    Returns all movie titles sorted alphabetically.
    """
    return sorted(movies['title'].tolist())


# Test
if __name__ == "__main__":

    movie = input("Enter Movie Name: ")

    result = recommend(movie)

    if result is None:
        print("\nMovie not found!")

    else:
        print("\nRecommended Movies:\n")

        for i, m in enumerate(result, start=1):
            print(f"{i}. {m}")