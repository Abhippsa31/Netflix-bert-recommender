import streamlit as st
from utils import set_background, search_youtube_trailer, load_data, embed_query, recommend_by_semantics

# -------------------- UI Setup --------------------
st.set_page_config(page_title="Netflix Recommender", layout="wide")
st.markdown(set_background("asserts/bg.png"), unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: black;'>🎬 Netflix Recommender</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: black;'>Find the perfect show or movie</p>", unsafe_allow_html=True)

# -------------------- Load Data & Model --------------------
with st.spinner("📦 Loading data..."):
    df, embeddings, model = load_data()

# -------------------- User Input --------------------
query = st.text_input("🔍 What are you in the mood for?", placeholder="e.g. dystopian future, romantic comedy, intense thriller")

if st.button("🎯 Recommend"):
    if not query.strip():
        st.warning("Please enter a theme, genre, or mood to get recommendations.")
    else:
        query_embedding = embed_query(query, model)
        results = recommend_by_semantics(query_embedding, embeddings, df)

        for _, row in results.iterrows():
            st.markdown(f"### 🎞️ {row['title']}")
            st.markdown(f"**Genres:** {row['listed_in']}")
            st.markdown(f"**Description:** {row['description']}")
            trailer_url = search_youtube_trailer(row['title'])

            if "watch?v=" in trailer_url:
                st.video(trailer_url)
            else:
                st.markdown(f"[🔗 Watch trailer on YouTube]({trailer_url})")

            st.markdown("---")
