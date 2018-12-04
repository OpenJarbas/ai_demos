import requests


def NER(text):
    data = {"model": "en_core_web_lg", "text": text}
    r = requests.post("https://api.explosion.ai/displacy/ent", data)
    return r.json()

