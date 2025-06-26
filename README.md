# 🧠 MindLytics – Mental Health & Sentiment Analytics from Reddit

**MindLytics** is an intelligent sentiment and emotion analysis platform that helps understand users' emotional state through Reddit posts or custom-written input. It provides emotion classification, mental health suggestions, song recommendations, and visual analytics like mood trends and word clouds.

---

## 🚀 Features

- 🔍 **Analyze Custom Text**: Detect emotional tone, get personalized mental health advice and songs.
- 👤 **Analyze Reddit Users**: Enter a Reddit username to fetch recent posts and analyze sentiment trends.
- 📈 **Visual Dashboard**: Displays emotion trend over time, mood distribution bar chart, and word cloud.
- 💬 **Toxicity Detection**: Uses Detoxify to flag harmful or threatening text.
- 🎧 **Mood-Based Music Recommender**: Suggests songs based on predicted mood.
- 🧠 **Mental Health Suggestions**: Personalized guidance based on dominant emotion.

---

## 📦 Folder Structure

```
MindLytics/
├── app.py
├── model/
│   └── emotion_classifier.py
├── utils/
│   ├── fetch_reddit.py
│   ├── song_recommender.py
│   ├── text_preprocessor.py
│   └── emotion_mapper.py
├── requirements.txt
└── README.md
```

---

## 🛠️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/MindLytics.git
cd MindLytics
```

### 2. Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

> ⚠️ Make sure you have a stable internet connection for Detoxify model download (~400MB).

---

## 🧪 Running the App

```bash
streamlit run app.py
```

Then open: [http://localhost:8501](http://localhost:8501)

---

## 🔑 Reddit API Setup

To fetch Reddit posts:

1. Go to [https://www.reddit.com/prefs/apps](https://www.reddit.com/prefs/apps)
2. Create an app with:
   - **name**: mindlytics-agent
   - **type**: script
   - **redirect URI**: [http://localhost:8000](http://localhost:8000)
3. Copy the **client ID** and **client secret**
4. Paste them into the app sidebar when using Reddit analysis.

---

## 🤖 Built With

- [Streamlit](https://streamlit.io/) — Web UI
- [Transformers](https://huggingface.co/transformers) — Emotion classifier
- [Detoxify](https://github.com/unitaryai/detoxify) — Toxicity detection
- [PRAW](https://praw.readthedocs.io/) — Reddit API wrapper
- [Matplotlib](https://matplotlib.org/) & [WordCloud](https://amueller.github.io/word_cloud/) — Visualization
- [Pandas](https://pandas.pydata.org/) — Data handling

---

## 📜 Example Inputs

### Custom Text

> “I feel really lost and empty these days.”

### Reddit Username

> `example_user123`

---

## 🧠 Mental Health Suggestions

Based on the most detected mood:

- **Depressed** → Helpline info, therapy suggestion
- **Anxious** → Breathing and journaling
- **Lonely** → Community recommendations
- **Happy** → Encouragement to share positivity
- *(and more...)*

---

## ✅ TODO (Future Scope)

- ✅ Add user-level dashboard history
- ✅ Integrate Spotify API for real song playback
- ⏳ Add GPT-based mental health Q&A
- ⏳ Deploy on Hugging Face or Render

---

## 🙏 Acknowledgments

- HuggingFace Transformers & Detoxify Team
- Reddit API (PRAW)
- Streamlit Community

---

## 📄 License

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

---

## 👩‍💻 Author

**Saakshi Pandey**  
