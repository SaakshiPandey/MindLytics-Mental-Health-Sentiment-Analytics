from transformers import pipeline

classifier = pipeline("text-classification", model="bhadresh-savani/bert-base-go-emotion", top_k=1)


def predict_emotion(text):
    result = classifier(text)[0]
    return result[0]["label"], round(result[0]["score"] * 100, 2)

