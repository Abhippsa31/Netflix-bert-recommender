# 🎬 Netflix Recommender

A semantic recommendation system built with **Streamlit** and **BERT embeddings** that helps users discover movies or shows on Netflix based on their mood, themes, or genres.

backgroud:
![bg](https://github.com/user-attachments/assets/c2bd474d-936c-437e-915b-1d3514763878)

---

## 🚀 Features

- 🌟 **Natural Language Query**: Type in phrases like _"romantic comedy"_ or _"post-apocalyptic thriller"_ to get curated results.
- 🔍 **Semantic Search**: Uses Sentence-BERT to recommend titles based on meaning, not just keywords.
- 📺 **YouTube Trailers**: Instantly watch trailers via YouTube integration.
- 🎨 Beautiful UI with background image support.

---

## 🧠 Tech Stack

- **Frontend/UI**: [Streamlit](https://streamlit.io)
- **ML Embeddings**: [Sentence-Transformers (MiniLM)](https://www.sbert.net/)
- **YouTube Integration**: Google API via `google-api-python-client`
- **Data**: Netflix titles dataset with precomputed clusters

---

## 🛠️ Installation

1. **Clone the repo**:

   ```bash
   git clone https://github.com/yourusername/netflix-recommender.git
   cd netflix-recommender
Install dependencies:
pip install -r requirements.txt
Add your YouTube API Key:
Open utils.py and insert your YouTube Data API v3 key:
YOUTUBE_API_KEY = "your_key_here"
Run the app:
streamlit run app.py

📁 Project Structure
bash
Copy
Edit
.
├── app.py                  # Streamlit app entry point
├── utils.py                # Functions: embedding, loading data, trailers
├── asserts/
│   └── bg.png              # Background image
├── netflix_titles_clustered.csv  # Netflix metadata (must be added)
├── requirements.txt


⚠️ Notes
You must add your own YouTube Data API Key for trailer functionality to work.

Ensure netflix_titles_clustered.csv is present in the root directory. You can create it by clustering metadata from a public Netflix dataset (e.g., from Kaggle) and adding a description, title, and listed_in column.

📸 Demo
A live demo is best served on Streamlit Community Cloud or HuggingFace Spaces.

📄 License
MIT License - free to use, modify, and share.

🙌 Acknowledgements
Netflix Movies and TV Shows Dataset

Sentence-Transformers

Streamlit
