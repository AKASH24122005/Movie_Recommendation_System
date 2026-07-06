# 🎬 Movie Recommendation System

A Content-Based Movie Recommendation System built using Python, Machine Learning, and Streamlit. The application recommends similar movies based on genres, keywords, cast, director, and movie overviews using TF-IDF Vectorization and Cosine Similarity.

---

## Features

- Content-Based Recommendation System
- Search from thousands of movies
- Top 5 similar movie recommendations
- Interactive Streamlit interface
- Machine Learning powered recommendations

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-Learn
- Streamlit
- Pickle

---

## Machine Learning Concepts

- Content-Based Filtering
- TF-IDF Vectorization
- Cosine Similarity
- Feature Engineering
- Natural Language Processing

---

## Project Structure

```text
Movie_Recommendation_System/
│
├── app.py
├── recommendation.py
├── train_model.py
├── requirements.txt
├── README.md
├── LICENSE
│
├── data/
│   ├── tmdb_5000_movies.csv
│   └── tmdb_5000_credits.csv
│
├── model/
│   ├── movies.pkl
│   └── similarity.pkl
│
├── screenshots/
│   ├── home.png
│   └── result.png
```

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/Movie_Recommendation_System.git
```

Navigate to the project:

```bash
cd Movie_Recommendation_System
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Train the model:

```bash
python train_model.py
```

Run the application:

```bash
streamlit run app.py
```

## Dataset

TMDB 5000 Movie Dataset

Files used:

- tmdb_5000_movies.csv
- tmdb_5000_credits.csv

## Future Improvements

- Movie posters using TMDB API
- Movie ratings
- Movie trailers
- Search suggestions
- Genre filtering
- Hybrid recommendation system

## Author

**Akash T**

GitHub: https://github.com/AKASH24122005

LinkedIn: *(Add your LinkedIn profile link here if desired)*

## License

This project is licensed under the MIT License.