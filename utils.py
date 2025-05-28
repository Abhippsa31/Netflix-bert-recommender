import pandas as pd
import numpy as np
import base64
from sentence_transformers import SentenceTransformer, util
from googleapiclient.discovery import build

YOUTUBE_API_KEY = "AIzaSyB14rW9L20OC6qfrsRBTju9yVV1KLaqu4A"  # Add your API key here

# ---------- Background Image Setter ----------
def set_background(image_path):
    with open(image_path, "rb") as img_file:
        encoded = base64.b64encode(img_file.read()).decode()
    return f"""
        <style>
        .stApp {{
            background-image: url("data:asserts/bg.png;base64,{encoded}");
            background-size: cover;
            background-attachment: fixed;
        }}
        </style>
    """

# ---------- YouTube Trailer Search ----------
def search_youtube_trailer(title):
    try:
        youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)
        query = f"{title} Netflix trailer"
        request = youtube.search().list(
            q=query,
            part='snippet',
            type='video',
            maxResults=1
        )
        response = request.execute()
        video_id = response['items'][0]['id']['videoId']
        return f"https://www.youtube.com/watch?v={video_id}"
    except Exception as e:
        print(f"[YouTube API error] {e}")
        query_fallback = f"{title} Netflix trailer".replace(' ', '+')
        return f"https://www.youtube.com/results?search_query={query_fallback}"

# ---------- Load Data & Embeddings ----------
def load_data():
    df = pd.read_csv("netflix_titles_clustered.csv")
    df.fillna('', inplace=True)
    df['combined'] = df['title'] + ' ' + df['listed_in'] + ' ' + df['description']
    model = SentenceTransformer('all-MiniLM-L6-v2')
    embeddings = model.encode(df['combined'].tolist(), convert_to_tensor=True)
    return df, embeddings, model

# ---------- BERT Query Embedding ----------
def embed_query(query, model):
    return model.encode(query, convert_to_tensor=True)

# ---------- Semantic Recommendation ----------
def recommend_by_semantics(query_emb, embeddings, df, top_n=5):
    scores = util.cos_sim(query_emb, embeddings)[0]
    top_indices = np.argsort(-scores.cpu().numpy())[:top_n]
    return df.iloc[top_indices]
