import requests


def neuralcoref(text):
    params = {"text": text.replace(".", ",").replace("\n", ", ")}
    r = requests.get("https://coref.huggingface.co/coref", params=params).json()
    return r