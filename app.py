import streamlit as st
from model.emotion_classifier import predict_emotion
from utils.text_preprocessor import clean_text
from utils.song_recommender import get_songs_by_emotion
from utils.fetch_reddit import fetch_user_posts
from utils.emotion_mapper import map_emotion_to_mood
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from datetime import datetime
from detoxify import Detoxify

st.set_page_config(page_title="Mindlytics", layout="wide")
st.title("🧠 Mindlytics – Mental Health & Sentiment Analytics from Reddit")

st.sidebar.title("Input Settings")
input_type = st.sidebar.selectbox("Choose input type", ["Custom Text", "Reddit Username"])

def display_suggestions(mood):
    mood_insights = {
        "depressed": "🧠 Signs of depression detected — encourage seeking professional help, reaching out to loved ones, and exploring therapy or helplines.",
        "anxious": "🫁 Anxiety signals found — suggest calming practices like deep breathing, mindfulness apps, and guided meditations.",
        "happy": "🌈 Positive mood detected — inspire gratitude journaling, sharing good news, and uplifting others in the community.",
        "anger": "🔥 Elevated anger detected — recommend taking a pause, practicing grounding exercises, or expressing emotions through art or journaling.",
        "loneliness": "🤍 Feelings of loneliness sensed — gently suggest connecting through online communities, support groups, or meaningful conversations.",
        "romantic": "💞 Romantic themes observed — promote healthy communication, self-love, and respectful relationship advice.",
        "hurt": "💔 Emotional pain noticed — offer comforting music, support group links, and reflective writing prompts to process feelings.",
        "neutral": "🔘 Neutral state detected — encourage engaging in light activities, creative hobbies, or moments of self-reflection.",
        "pride": "💫 Prideful expression — channel it into positive affirmation, goal visualization, or mentorship opportunities.",
        "excitement": "🚀 High excitement sensed — recommend setting achievable goals, capturing the moment in a journal, or celebrating small wins."
    }

    suggestion = mood_insights.get(mood, "No specific recommendation available.")
    st.markdown(f"💡 **Suggestion:** {suggestion}")

def is_text_toxic(text):
    result = Detoxify('original').predict(text)
    return result['toxicity'] > 0.5 or result['threat'] > 0.4

# ============ Custom Text Input ============= #
if input_type == "Custom Text":
    user_input = st.text_area("Write something you're feeling...")

    if st.button("Analyze"):
        clean = clean_text(user_input)

        if is_text_toxic(clean):
            st.error("🚨 Harmful or violent content detected. Please reach out to a professional or helpline immediately.")
            st.stop()
        else:
            emotion, score = predict_emotion(clean)
            mapped_mood = map_emotion_to_mood(emotion)

            st.success(f"Emotion Detected: `{emotion}` ({score}%) → Mood Category: `{mapped_mood}`")

            st.subheader("🎧 Song Suggestions:")
            songs = get_songs_by_emotion(mapped_mood)
            if songs:
                for song in songs:
                    st.markdown(f"- **{song['title']}** by *{song['artist']}*")
            else:
                st.warning("No songs available for this mood yet.")

            st.subheader("🧠 Mental Health Insight & Suggestion")
            display_suggestions(mapped_mood)

# ============ Reddit Username Input ============= #
else:
    client_id = st.sidebar.text_input("Reddit Client ID")
    client_secret = st.sidebar.text_input("Reddit Client Secret", type="password")
    username = st.sidebar.text_input("Reddit Username")
    limit = st.sidebar.slider("Number of Posts", 1, 20, 5)

    if st.sidebar.button("Fetch & Analyze"):
        try:
            posts = fetch_user_posts(client_id, client_secret, "mindlytics-agent", username, limit)
        except Exception as e:
            st.error("Failed to fetch Reddit posts. Please check credentials and username.")
            st.stop()

        if not posts:
            st.warning("No posts found for this user.")
            st.stop()

        data = []

        for post in posts:
            text = clean_text(post["title"] + " " + post["content"])
            if not text.strip():
                continue

            emotion, score = predict_emotion(text)
            mapped_mood = map_emotion_to_mood(emotion)
            timestamp = pd.to_datetime(post.get("created", datetime.now().timestamp()), unit="s")

            data.append({
                "text": text[:100],
                "emotion": emotion,
                "mapped_mood": mapped_mood,
                "score": score,
                "timestamp": timestamp
            })

        if not data:
            st.warning("All posts were empty or unsuitable for analysis.")
            st.stop()

        df = pd.DataFrame(data)

        st.markdown("## 📊 Emotion Analytics Dashboard")
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("📋 Raw Analysis")
            st.dataframe(df)

        with col2:
            st.subheader("📈 Emotion Trend Over Time")
            if "timestamp" in df.columns and not df["timestamp"].isnull().all():
                df["date"] = pd.to_datetime(df["timestamp"], errors='coerce').dt.date
                trend = df.groupby(["date", "mapped_mood"]).size().unstack().fillna(0)
                st.line_chart(trend)
            else:
                st.warning("No valid timestamps available to display the emotion trend.")

        st.subheader("🔢 Mood Distribution")
        if "mapped_mood" in df.columns:
            st.bar_chart(df["mapped_mood"].value_counts())
        else:
            st.warning("No mood data to show.")

        st.subheader("☁️ Word Cloud")
        words = " ".join(df["text"].tolist())
        wc = WordCloud(background_color="white").generate(words)
        st.image(wc.to_array(), use_column_width=True)

        st.subheader("🧠 Mental Health Insight & Suggestion")
        most_common = df["mapped_mood"].value_counts().idxmax()
        st.info(f"**Most Prevalent Mood:** `{most_common}`")
        display_suggestions(most_common)
