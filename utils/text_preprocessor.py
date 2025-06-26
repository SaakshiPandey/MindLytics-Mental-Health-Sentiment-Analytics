import re

def clean_text(text):
    text = re.sub(r"http\S+|www\S+|@\S+|#\S+", "", text)
    text = re.sub(r"[^A-Za-z0-9\s]", "", text)
    return text.lower().strip()
