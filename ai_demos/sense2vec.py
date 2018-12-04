import requests


def similar(text, sense="auto"):
    data = {"word": text, "sense": sense}
    r = requests.post("https://api.explosion.ai/sense2vec/find", data)
    return r.json()
