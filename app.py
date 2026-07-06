import streamlit as st
from recommendation import recommend, get_movie_titles

# ----------------------------------------------------
# Page Configuration
# ----------------------------------------------------
st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬",
    layout="wide"
)

# ----------------------------------------------------
# Custom CSS
# ----------------------------------------------------
st.markdown("""
<style>
.main{
    background-color:#0E1117;
}

.title{
    text-align:center;
    color:#00BFFF;
    font-size:42px;
    font-weight:bold;
}

.subtitle{
    text-align:center;
    color:white;
    font-size:18px;
}

.movie{
    background-color:#262730;
    padding:15px;
    border-radius:10px;
    margin-bottom:10px;
    color:white;
    font-size:18px;
}
</style>
""", unsafe_allow_html=True)

# ----------------------------------------------------
# Sidebar
# ----------------------------------------------------
st.sidebar.title("About")

st.sidebar.info("""
Content-Based Movie Recommendation System

Technology Used

• Python

• Streamlit

• Pandas

• Scikit-Learn

• TF-IDF

• Cosine Similarity
""")

# ----------------------------------------------------
# Title
# ----------------------------------------------------
st.markdown(
    "<p class='title'>🎬 Movie Recommendation System</p>",
    unsafe_allow_html=True
)

st.markdown(
    "<p class='subtitle'>Find similar movies using Machine Learning</p>",
    unsafe_allow_html=True
)

st.write("")

# ----------------------------------------------------
# Movie Selection
# ----------------------------------------------------
movie_titles = get_movie_titles()

selected_movie = st.selectbox(
    "Select a Movie",
    movie_titles
)

# ----------------------------------------------------
# Recommendation Button
# ----------------------------------------------------
if st.button("Recommend Movies"):

    recommendations = recommend(selected_movie)

    st.write("")

    st.subheader("Recommended Movies")

    for i, movie in enumerate(recommendations, start=1):

        st.markdown(
            f"<div class='movie'>{i}. {movie}</div>",
            unsafe_allow_html=True
        )