def map_emotion_to_mood(emotion):
    emotion = emotion.lower()

    mapping = {
        "love": "romantic",
        "desire": "romantic",

        "excitement": "excitement",
        "amusement": "excitement",
        "enthusiasm": "excitement",

        "happy": "happy",
        "fun": "happy",
        "gratitude": "happy",
        "approval": "happy",

        "joy": "joy",
        "optimism": "joy",
        "admiration": "joy",
        "realization": "joy",

        "pride": "pride",
        "confidence": "pride",

        "nervousness": "nervous",
        "anticipation": "nervous",

        "fear": "anxious",
        "embarrassment": "anxious",
        "remorse": "anxious",
        "confusion": "anxious",

        "anger": "anger",
        "annoyance": "anger",
        "disgust": "anger",

        "hurt": "hurt",

        "sadness": "depressed",
        "grief": "depressed",
        "disappointment": "depressed",

        "loneliness": "loneliness",
        "isolation": "loneliness",

        "neutral": "neutral",
        "boredom": "neutral",
        "curiosity": "neutral",

        "surprise": "surprise",
        "shock": "surprise"
    }

    return mapping.get(emotion, "neutral")
