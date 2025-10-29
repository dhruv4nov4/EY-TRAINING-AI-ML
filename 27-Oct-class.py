from transformers import pipeline

sentiment_pipeline = pipeline(model="finiteautomata/bertweet-base-sentiment-analysis")

data = [
    "I had an amazing day at work today!",
    "The food tasted awful and cold.",
    "The new phone update is okay, nothing special.",
    "This game is so addictive and fun to play!",
    "I waited an hour for the bus, totally frustrated."
]

results = sentiment_pipeline(data)
print(results)